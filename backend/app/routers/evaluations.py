import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.interview import Interview
from app.models.answer import Answer
from app.utils.auth import get_current_user
from app.ai.answer_evaluator import evaluate_answer

router = APIRouter(prefix="/evaluations", tags=["Evaluations"])


@router.get("/{interview_id}")
def get_evaluation_report(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Full interview report with per-question answers and evaluations."""
    interview = db.query(Interview).filter(
        Interview.id == interview_id,
        Interview.user_id == current_user.id
    ).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")

    answers = db.query(Answer).filter(Answer.interview_id == interview_id).all()

    answers_data = []
    for ans in answers:
        eval_data = None
        if ans.evaluation:
            e = ans.evaluation
            eval_data = {
                "relevance_score": e.relevance_score,
                "accuracy_score": e.accuracy_score,
                "completeness_score": e.completeness_score,
                "similarity_score": e.similarity_score,
                "communication_score": e.communication_score,
                "overall_score": e.overall_score,
                "feedback": e.feedback,
                "strengths": json.loads(e.strengths) if e.strengths else [],
                "improvements": json.loads(e.improvements) if e.improvements else [],
            }
        answers_data.append({
            "answer_id": ans.id,
            "question_text": ans.question_text,
            "answer_text": ans.answer_text,
            "duration_seconds": ans.duration_seconds,
            "submitted_at": ans.submitted_at,
            "evaluation": eval_data,
        })

    return {
        "interview": {
            "id": interview.id,
            "role_name": interview.role_name,
            "difficulty": interview.difficulty,
            "mode": interview.mode,
            "total_questions": interview.total_questions,
            "questions_answered": interview.questions_answered,
            "overall_score": interview.overall_score,
            "technical_score": interview.technical_score,
            "relevance_score": interview.relevance_score,
            "completeness_score": interview.completeness_score,
            "communication_score": interview.communication_score,
            "status": interview.status,
            "strong_areas": json.loads(interview.strong_areas) if interview.strong_areas else [],
            "weak_areas": json.loads(interview.weak_areas) if interview.weak_areas else [],
            "recommendations": json.loads(interview.recommendations) if interview.recommendations else [],
            "started_at": interview.started_at,
            "completed_at": interview.completed_at,
        },
        "answers": answers_data,
    }


@router.post("/evaluate/text")
def evaluate_single_answer(
    data: dict,
    current_user: User = Depends(get_current_user),
):
    """Evaluate a single answer on-the-fly (for testing/demo)."""
    result = evaluate_answer(
        question_text=data.get("question_text", ""),
        expected_answer=data.get("expected_answer", ""),
        expected_concepts=data.get("expected_concepts", []),
        student_answer=data.get("student_answer", ""),
    )
    return result
