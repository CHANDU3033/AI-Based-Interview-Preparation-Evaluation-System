import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Question Generation Engine
===========================
Provides questions for interview sessions via:
  1. DB question bank (primary, deterministic with strict deduplication)
  2. Groq AI generation (supplemental, when available)
  3. Resume-Skill tailored questions + General role questions mix
"""

import json
import logging
import random
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.question import Question
from app.ai.groq_engine import generate_interview_questions as groq_generate, is_groq_available

logger = logging.getLogger(__name__)


def extract_skills_from_text(text: str) -> List[str]:
    """Extract technical keywords from resume text."""
    if not text:
        return []
    keywords = [
        "python", "django", "fastapi", "flask", "java", "spring", "c++", 
        "javascript", "typescript", "react", "node", "angular", "vue", 
        "sql", "postgresql", "mysql", "mongodb", "aws", "docker", 
        "kubernetes", "terraform", "machine learning", "pandas", "numpy",
        "scikit-learn", "rest api", "graphql", "redis", "linux", "git",
        "data structures", "algorithms"
    ]
    found = []
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            found.append(kw.title())
    return list(set(found))


def get_questions_from_db(
    db: Session,
    role_id: int,
    difficulty: str,
    count: int,
) -> List[Question]:
    """Fetch distinct random questions from DB for the given role and difficulty."""
    questions = (
        db.query(Question)
        .filter(Question.role_id == role_id, Question.difficulty == difficulty)
        .all()
    )

    if len(questions) < count:
        all_q = db.query(Question).filter(Question.role_id == role_id).all()
        questions = all_q

    # Deduplicate questions by normalized question_text
    seen_texts = set()
    unique_q = []
    for q in questions:
        norm_text = q.question_text.strip().lower()
        if norm_text not in seen_texts:
            seen_texts.add(norm_text)
            unique_q.append(q)

    # Use random.sample to guarantee completely distinct, non-repeating items
    sample_size = min(count, len(unique_q))
    return random.sample(unique_q, sample_size) if sample_size > 0 else []


def generate_ai_questions(
    role_name: str,
    difficulty: str,
    count: int,
    previous_questions: List[str] = [],
) -> List[dict]:
    """Generate questions via Groq. Returns list of question dicts."""
    if not is_groq_available():
        return []
    result = groq_generate(role_name, difficulty, count, previous_questions)
    return result or []


def get_hybrid_questions(
    db: Session,
    role_id: int,
    role_name: str,
    difficulty: str,
    total_count: int,
    resume_text: Optional[str] = None,
) -> List[dict]:
    """
    Hybrid strategy with strict deduplication:
    - If resume_text provided: 60% Resume-Skill questions + 40% General Role questions.
    - If no resume_text: DB questions filtered by role & difficulty.
    Guarantees that NO question is ever repeated.
    """
    skills = extract_skills_from_text(resume_text) if resume_text else []
    
    final_questions = []
    used_ids = set()
    used_texts = set()

    def add_question(q_dict):
        q_id = q_dict.get("id")
        norm_text = q_dict["question_text"].strip().lower()
        if (q_id and q_id in used_ids) or (norm_text in used_texts):
            return False
        if q_id:
            used_ids.add(q_id)
        used_texts.add(norm_text)
        final_questions.append(q_dict)
        return True

    if skills:
        resume_count = max(1, int(total_count * 0.6))
        all_db_q = db.query(Question).all()
        random.shuffle(all_db_q)

        for q in all_db_q:
            q_text_lower = q.question_text.lower()
            q_concepts_lower = q.expected_concepts.lower() if q.expected_concepts else ""
            
            for sk in skills:
                sk_lower = sk.lower()
                if sk_lower in q_text_lower or sk_lower in q_concepts_lower:
                    concepts = []
                    try:
                        concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
                    except Exception:
                        pass
                    
                    added = add_question({
                        "id": q.id,
                        "question_text": f"[Resume Skill: {sk}] {q.question_text}",
                        "category": f"Resume Skill ({sk})",
                        "difficulty": q.difficulty,
                        "expected_answer": q.expected_answer or "",
                        "expected_concepts": concepts,
                        "is_ai_generated": False,
                    })
                    if added and len(final_questions) >= resume_count:
                        break
            if len(final_questions) >= resume_count:
                break

    # Fill remaining / primary questions from DB matching role and difficulty
    if len(final_questions) < total_count:
        needed = total_count - len(final_questions)
        db_qs = get_questions_from_db(db, role_id, difficulty, needed * 3)
        for q in db_qs:
            if len(final_questions) >= total_count:
                break
            concepts = []
            try:
                concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
            except Exception:
                pass
            add_question({
                "id": q.id,
                "question_text": q.question_text,
                "category": q.category or "Technical",
                "difficulty": q.difficulty,
                "expected_answer": q.expected_answer or "",
                "expected_concepts": concepts,
                "is_ai_generated": False,
            })

    # Extra safety net: If for any reason total_count is still not reached, fill from all questions of role
    if len(final_questions) < total_count:
        all_role_qs = db.query(Question).filter(Question.role_id == role_id).all()
        random.shuffle(all_role_qs)
        for q in all_role_qs:
            if len(final_questions) >= total_count:
                break
            concepts = []
            try:
                concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
            except Exception:
                pass
            add_question({
                "id": q.id,
                "question_text": q.question_text,
                "category": q.category or "Technical",
                "difficulty": q.difficulty,
                "expected_answer": q.expected_answer or "",
                "expected_concepts": concepts,
                "is_ai_generated": False,
            })

    return final_questions[:total_count]
