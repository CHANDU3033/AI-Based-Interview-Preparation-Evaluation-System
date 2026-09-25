import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
import json
from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.question import JobRole, Question
from app.models.interview import Interview
from app.models.answer import Answer
from app.models.evaluation import Evaluation
from app.schemas.interview import (
    InterviewStartRequest, InterviewResponse, InterviewDetailResponse,
    AnswerSubmitRequest, AnswerSubmitResponse,
)
from app.utils.auth import get_current_user
from app.ai.question_generator import get_hybrid_questions
from app.ai.answer_evaluator import evaluate_answer

router = APIRouter(prefix="/interviews", tags=["Interviews"])


def _get_interview_or_404(interview_id: int, user_id: int, db: Session) -> Interview:
    interview = db.query(Interview).filter(
        Interview.id == interview_id,
        Interview.user_id == user_id
    ).first()
    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")
    return interview


@router.post("/start", status_code=status.HTTP_201_CREATED)
def start_interview(
    request: InterviewStartRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Start a new interview session."""
    # Validate role
    role = db.query(JobRole).filter(JobRole.id == request.role_id, JobRole.is_active == True).first()
    if not role:
        raise HTTPException(status_code=404, detail="Job role not found")

    # Get questions (hybrid: DB + AI)
    questions = get_hybrid_questions(
        db=db,
        role_id=role.id,
        role_name=role.role_name,
        difficulty=request.difficulty,
        total_count=request.total_questions,
        resume_text=request.resume_text,
    )

    if not questions:
        raise HTTPException(status_code=404, detail="No questions available for this role/difficulty")

    # Store question data as JSON in interview
    question_data_json = json.dumps(questions)

    interview = Interview(
        user_id=current_user.id,
        role_id=role.id,
        role_name=role.role_name,
        difficulty=request.difficulty,
        mode=request.mode,
        total_questions=len(questions),
        question_ids=question_data_json,
        questions_answered=0,
        status="IN_PROGRESS",
    )
    db.add(interview)
    db.commit()
    db.refresh(interview)

    # Return first question
    first_question = questions[0]
    return {
        "interview_id": interview.id,
        "role_name": role.role_name,
        "difficulty": request.difficulty,
        "mode": request.mode,
        "total_questions": len(questions),
        "current_question": {
            "index": 0,
            "id": first_question.get("id"),
            "question_text": first_question["question_text"],
            "category": first_question["category"],
            "difficulty": first_question["difficulty"],
        },
    }


@router.get("/history")
def get_interview_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get user's past interviews (newest first)."""
    interviews = (
        db.query(Interview)
        .filter(Interview.user_id == current_user.id)
        .order_by(Interview.started_at.desc())
        .all()
    )
    return [
        {
            "id": iv.id,
            "role_name": iv.role_name,
            "difficulty": iv.difficulty,
            "mode": iv.mode,
            "total_questions": iv.total_questions,
            "questions_answered": iv.questions_answered,
            "overall_score": iv.overall_score,
            "status": iv.status,
            "started_at": iv.started_at,
            "completed_at": iv.completed_at,
        }
        for iv in interviews
    ]


@router.get("/{interview_id}")
def get_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get current interview state with the next unanswered question."""
    interview = _get_interview_or_404(interview_id, current_user.id, db)

    questions = json.loads(interview.question_ids or "[]")
    idx = interview.questions_answered

    current_question = None
    if idx < len(questions):
        q = questions[idx]
        current_question = {
            "index": idx,
            "id": q.get("id"),
            "question_text": q["question_text"],
            "category": q["category"],
            "difficulty": q["difficulty"],
        }

    return {
        "id": interview.id,
        "role_name": interview.role_name,
        "difficulty": interview.difficulty,
        "mode": interview.mode,
        "total_questions": interview.total_questions,
        "questions_answered": interview.questions_answered,
        "status": interview.status,
        "current_question": current_question,
        "overall_score": interview.overall_score,
    }


@router.post("/{interview_id}/answer")
def submit_answer(
    interview_id: int,
    answer_request: AnswerSubmitRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Submit an answer, evaluate it, and return next question."""
    interview = _get_interview_or_404(interview_id, current_user.id, db)

    if interview.status != "IN_PROGRESS":
        raise HTTPException(status_code=400, detail="Interview is not in progress")

    questions = json.loads(interview.question_ids or "[]")
    idx = interview.questions_answered

    if idx >= len(questions):
        raise HTTPException(status_code=400, detail="All questions already answered")

    current_q = questions[idx]

    # Save answer
    answer = Answer(
        interview_id=interview.id,
        question_id=answer_request.question_id or (current_q.get("id") or 0),
        question_text=current_q["question_text"],
        answer_text=answer_request.answer_text,
        duration_seconds=answer_request.duration_seconds,
    )
    db.add(answer)
    db.flush()

    # Evaluate answer
    expected_concepts = current_q.get("expected_concepts", [])
    if isinstance(expected_concepts, str):
        try:
            expected_concepts = json.loads(expected_concepts)
        except Exception:
            expected_concepts = []

    eval_result = evaluate_answer(
        question_text=current_q["question_text"],
        expected_answer=current_q.get("expected_answer", ""),
        expected_concepts=expected_concepts,
        student_answer=answer_request.answer_text,
        duration_seconds=answer_request.duration_seconds,
    )

    # Save evaluation
    evaluation = Evaluation(
        answer_id=answer.id,
        relevance_score=eval_result.get("relevance_score", 0),
        accuracy_score=eval_result.get("accuracy_score", 0),
        completeness_score=eval_result.get("completeness_score", 0),
        similarity_score=eval_result.get("similarity_score", 0),
        communication_score=eval_result.get("communication_score", 0),
        overall_score=eval_result.get("overall_score", 0),
        feedback=eval_result.get("feedback", ""),
        strengths=json.dumps(eval_result.get("strengths", [])),
        improvements=json.dumps(eval_result.get("improvements", [])),
    )
    db.add(evaluation)

    # Advance interview
    interview.questions_answered = idx + 1
    interview_complete = interview.questions_answered >= interview.total_questions

    # Get next question
    next_question = None
    if not interview_complete:
        nq = questions[idx + 1]
        next_question = {
            "index": idx + 1,
            "id": nq.get("id"),
            "question_text": nq["question_text"],
            "category": nq["category"],
            "difficulty": nq["difficulty"],
        }

    db.commit()

    return {
        "answer_id": answer.id,
        "question_id": answer.question_id,
        "evaluation": {
            **eval_result,
            "strengths": eval_result.get("strengths", []),
            "improvements": eval_result.get("improvements", []),
        },
        "next_question": next_question,
        "interview_complete": interview_complete,
        "questions_answered": interview.questions_answered,
        "total_questions": interview.total_questions,
    }


@router.post("/{interview_id}/complete")
def complete_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Complete the interview and compute aggregate scores."""
    interview = _get_interview_or_404(interview_id, current_user.id, db)

    if interview.status == "COMPLETED":
        return {"message": "Interview already completed", "interview_id": interview_id}

    # Get all evaluations for this interview
    answers = db.query(Answer).filter(Answer.interview_id == interview_id).all()
    evaluations = []
    for ans in answers:
        if ans.evaluation:
            evaluations.append(ans.evaluation)

    if evaluations:
        overall_score = sum(e.overall_score for e in evaluations) / len(evaluations)
        technical_score = sum(e.accuracy_score for e in evaluations) / len(evaluations)
        relevance_score = sum(e.relevance_score for e in evaluations) / len(evaluations)
        completeness_score = sum(e.completeness_score for e in evaluations) / len(evaluations)
        communication_score = sum(e.communication_score for e in evaluations) / len(evaluations)
    else:
        overall_score = technical_score = relevance_score = completeness_score = communication_score = 0

    # Determine strong/weak areas based on scores
    score_map = {
        "Technical Knowledge": technical_score,
        "Answer Relevance": relevance_score,
        "Completeness": completeness_score,
        "Communication": communication_score,
    }
    strong_areas = [k for k, v in score_map.items() if v >= 75]
    weak_areas = [k for k, v in score_map.items() if v < 65]

    # Simple recommendations
    recommendations = []
    if technical_score < 70:
        recommendations.append(f"Study more {interview.role_name} technical concepts")
    if completeness_score < 70:
        recommendations.append("Practice giving more complete and structured answers")
    if communication_score < 70:
        recommendations.append("Work on clarity and avoid filler words")
    if relevance_score < 70:
        recommendations.append("Focus on answering the specific question asked")
    if not recommendations:
        recommendations.append("Excellent performance! Keep practicing advanced topics")

    interview.overall_score = round(overall_score, 1)
    interview.technical_score = round(technical_score, 1)
    interview.relevance_score = round(relevance_score, 1)
    interview.completeness_score = round(completeness_score, 1)
    interview.communication_score = round(communication_score, 1)
    interview.status = "COMPLETED"
    interview.completed_at = datetime.utcnow()
    interview.strong_areas = json.dumps(strong_areas)
    interview.weak_areas = json.dumps(weak_areas)
    interview.recommendations = json.dumps(recommendations)

    db.commit()

    return {
        "interview_id": interview_id,
        "status": "COMPLETED",
        "overall_score": interview.overall_score,
        "technical_score": interview.technical_score,
        "relevance_score": interview.relevance_score,
        "completeness_score": interview.completeness_score,
        "communication_score": interview.communication_score,
        "strong_areas": strong_areas,
        "weak_areas": weak_areas,
        "recommendations": recommendations,
    }


@router.delete("/{interview_id}")
def cancel_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Cancel an in-progress interview."""
    interview = _get_interview_or_404(interview_id, current_user.id, db)
    interview.status = "CANCELLED"
    db.commit()
    return {"message": "Interview cancelled", "interview_id": interview_id}


@router.post("/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    """Parse uploaded resume file (PDF or TXT) and extract skills."""
    filename = file.filename.lower()
    content = ""
    try:
        if filename.endswith(".pdf"):
            import pypdf
            reader = pypdf.PdfReader(file.file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    content += text + "\n"
        else:
            raw = await file.read()
            content = raw.decode("utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse resume file: {str(e)}")

    from app.ai.question_generator import extract_skills_from_text
    skills = extract_skills_from_text(content)
    return {"filename": file.filename, "resume_text": content.strip(), "skills": skills}
