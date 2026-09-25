import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Question Generation Engine
===========================
Provides questions for interview sessions via:
  1. DB question bank (primary, deterministic)
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
    """Fetch random questions from DB for the given role and difficulty."""
    questions = (
        db.query(Question)
        .filter(Question.role_id == role_id, Question.difficulty == difficulty)
        .all()
    )

    if len(questions) < count:
        all_q = db.query(Question).filter(Question.role_id == role_id).all()
        questions = all_q

    random.shuffle(questions)
    return questions[:count]


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
    Hybrid strategy:
    - If resume_text provided: 60% Resume-Skill questions + 40% General Role questions.
    - If no resume_text: 70% DB + 30% AI questions.
    """
    skills = extract_skills_from_text(resume_text) if resume_text else []
    
    final_questions = []
    used_ids = set()

    if skills:
        # Split: 60% Resume Skills, 40% General Role
        resume_count = max(1, int(total_count * 0.6))
        general_count = total_count - resume_count

        # 1. Fetch questions matching extracted resume skills from entire DB
        skill_matched_q = []
        all_db_q = db.query(Question).all()
        random.shuffle(all_db_q)

        for q in all_db_q:
            q_text_lower = q.question_text.lower()
            q_concepts_lower = q.expected_concepts.lower() if q.expected_concepts else ""
            
            for sk in skills:
                sk_lower = sk.lower()
                if sk_lower in q_text_lower or sk_lower in q_concepts_lower:
                    if q.id not in used_ids:
                        used_ids.add(q.id)
                        concepts = []
                        try:
                            concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
                        except Exception:
                            pass
                        
                        skill_matched_q.append({
                            "id": q.id,
                            "question_text": f"[Resume Skill: {sk}] {q.question_text}",
                            "category": f"Resume Skill ({sk})",
                            "difficulty": q.difficulty,
                            "expected_answer": q.expected_answer or "",
                            "expected_concepts": concepts,
                            "is_ai_generated": False,
                        })
                        break
            if len(skill_matched_q) >= resume_count:
                break

        final_questions.extend(skill_matched_q)

        # 2. Fetch general questions for role
        remaining_count = total_count - len(final_questions)
        general_db_q = get_questions_from_db(db, role_id, difficulty, remaining_count * 2)
        
        for q in general_db_q:
            if q.id not in used_ids and len(final_questions) < total_count:
                used_ids.add(q.id)
                concepts = []
                try:
                    concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
                except Exception:
                    pass
                
                final_questions.append({
                    "id": q.id,
                    "question_text": q.question_text,
                    "category": q.category or "General Technical",
                    "difficulty": q.difficulty,
                    "expected_answer": q.expected_answer or "",
                    "expected_concepts": concepts,
                    "is_ai_generated": False,
                })

    # Fallback or standard flow if no resume or not enough skill matches
    if len(final_questions) < total_count:
        needed = total_count - len(final_questions)
        standard_q = get_questions_from_db(db, role_id, difficulty, needed)
        for q in standard_q:
            if q.id not in used_ids and len(final_questions) < total_count:
                used_ids.add(q.id)
                concepts = []
                try:
                    concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
                except Exception:
                    pass
                final_questions.append({
                    "id": q.id,
                    "question_text": q.question_text,
                    "category": q.category,
                    "difficulty": q.difficulty,
                    "expected_answer": q.expected_answer or "",
                    "expected_concepts": concepts,
                    "is_ai_generated": False,
                })

    return final_questions[:total_count]
