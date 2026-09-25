import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Question Generation Engine
===========================
Provides questions for interview sessions via:
  1. DB question bank (primary, deterministic)
  2. Groq AI generation (supplemental, when available)
  3. Hybrid mix (70% DB + 30% AI)
"""

import json
import logging
import random
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.question import Question
from app.ai.groq_engine import generate_interview_questions as groq_generate, is_groq_available

logger = logging.getLogger(__name__)


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

    # If not enough, pull from adjacent difficulties
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
) -> List[dict]:
    """
    Hybrid strategy: 70% from DB + 30% from Groq AI.
    Returns list of question dicts ready for interview session.
    """
    db_count = max(int(total_count * 0.7), 1)
    ai_count = total_count - db_count

    db_questions = get_questions_from_db(db, role_id, difficulty, db_count)
    db_q_dicts = []
    prev_texts = []

    for q in db_questions:
        concepts = []
        try:
            concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
        except Exception:
            pass
        db_q_dicts.append({
            "id": q.id,
            "question_text": q.question_text,
            "category": q.category,
            "difficulty": q.difficulty,
            "expected_answer": q.expected_answer or "",
            "expected_concepts": concepts,
            "is_ai_generated": False,
        })
        prev_texts.append(q.question_text)

    # Fill with AI-generated questions if Groq available
    ai_q_dicts = []
    if ai_count > 0 and is_groq_available():
        ai_results = generate_ai_questions(role_name, difficulty, ai_count, prev_texts)
        for q in ai_results:
            ai_q_dicts.append({
                "id": None,  # not in DB
                "question_text": q.get("question_text", ""),
                "category": q.get("category", "Technical"),
                "difficulty": difficulty,
                "expected_answer": q.get("expected_answer", ""),
                "expected_concepts": q.get("expected_concepts", []),
                "is_ai_generated": True,
            })

    all_questions = db_q_dicts + ai_q_dicts
    random.shuffle(all_questions)

    # Ensure we have exactly total_count (top up from DB if AI fails)
    if len(all_questions) < total_count:
        extra = get_questions_from_db(db, role_id, difficulty, total_count - len(all_questions))
        existing_ids = {q["id"] for q in all_questions if q["id"]}
        for q in extra:
            if q.id not in existing_ids:
                concepts = []
                try:
                    concepts = json.loads(q.expected_concepts) if q.expected_concepts else []
                except Exception:
                    pass
                all_questions.append({
                    "id": q.id,
                    "question_text": q.question_text,
                    "category": q.category,
                    "difficulty": q.difficulty,
                    "expected_answer": q.expected_answer or "",
                    "expected_concepts": concepts,
                    "is_ai_generated": False,
                })

    return all_questions[:total_count]
