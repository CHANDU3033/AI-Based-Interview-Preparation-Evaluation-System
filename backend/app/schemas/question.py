import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class JobRoleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role_name: str
    description: Optional[str] = None
    is_active: bool


class QuestionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role_id: int
    category: str
    difficulty: str
    question_text: str
    # NOTE: expected_answer NOT exposed to student during interview


class GenerateQuestionsRequest(BaseModel):
    role_name: str
    difficulty: str = "Intermediate"
    count: int = 5
    previous_questions: List[str] = []
