import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime


class EvaluationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    answer_id: int
    relevance_score: float
    accuracy_score: float
    completeness_score: float
    similarity_score: float
    communication_score: float
    overall_score: float
    feedback: Optional[str] = None
    strengths: Optional[List[str]] = None
    improvements: Optional[List[str]] = None
    created_at: datetime


class DashboardResponse(BaseModel):
    total_interviews: int
    avg_score: float
    best_score: float
    recent_interviews: List[dict]
    score_progression: List[dict]   # [{date, score}, ...]
    weak_topics: List[str]
    strong_topics: List[str]
    recommendations: List[str]
