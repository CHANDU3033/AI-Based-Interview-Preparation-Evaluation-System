import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime


class InterviewStartRequest(BaseModel):
    role_id: int
    difficulty: str = "Intermediate"   # Beginner | Intermediate | Advanced
    mode: str = "TEXT"                 # TEXT | VOICE
    total_questions: int = 10


class InterviewResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    role_name: str
    difficulty: str
    mode: str
    total_questions: int
    questions_answered: int
    overall_score: Optional[float] = None
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None


class InterviewDetailResponse(InterviewResponse):
    technical_score: Optional[float] = None
    relevance_score: Optional[float] = None
    completeness_score: Optional[float] = None
    communication_score: Optional[float] = None
    strong_areas: Optional[List[str]] = None
    weak_areas: Optional[List[str]] = None
    recommendations: Optional[List[str]] = None


class AnswerSubmitRequest(BaseModel):
    question_id: int
    answer_text: str
    duration_seconds: Optional[int] = None


class AnswerSubmitResponse(BaseModel):
    answer_id: int
    question_id: int
    evaluation: dict
    next_question: Optional[dict] = None
    interview_complete: bool = False
    questions_answered: int
    total_questions: int
