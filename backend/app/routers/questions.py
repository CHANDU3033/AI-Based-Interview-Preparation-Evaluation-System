import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.question import JobRole, Question
from app.models.user import User
from app.schemas.question import JobRoleResponse, QuestionResponse, GenerateQuestionsRequest
from app.utils.auth import get_current_user
from app.ai.question_generator import generate_ai_questions

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/roles", response_model=List[JobRoleResponse])
def get_job_roles(db: Session = Depends(get_db)):
    """Return all active job roles."""
    return db.query(JobRole).filter(JobRole.is_active == True).all()


@router.get("/{role_id}", response_model=List[QuestionResponse])
def get_questions_for_role(
    role_id: int,
    difficulty: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    """Get questions filtered by role, optionally by difficulty and category."""
    query = db.query(Question).filter(Question.role_id == role_id)
    if difficulty:
        query = query.filter(Question.difficulty == difficulty)
    if category:
        query = query.filter(Question.category == category)
    return query.limit(limit).all()


@router.post("/generate")
def generate_questions(
    request: GenerateQuestionsRequest,
    current_user: User = Depends(get_current_user),
):
    """AI-generate interview questions using Groq."""
    questions = generate_ai_questions(
        role_name=request.role_name,
        difficulty=request.difficulty,
        count=request.count,
        previous_questions=request.previous_questions,
    )
    if not questions:
        raise HTTPException(
            status_code=503,
            detail="AI question generation unavailable. Please configure GROQ_API_KEY."
        )
    return {"questions": questions, "count": len(questions)}
