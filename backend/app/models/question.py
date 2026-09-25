import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class JobRole(Base):
    __tablename__ = "job_roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    questions = relationship("Question", back_populates="job_role")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("job_roles.id"), nullable=False)  # FK to job_roles
    category = Column(String(50), nullable=False)    # Technical | HR | Project | Scenario
    difficulty = Column(String(20), nullable=False)  # Beginner | Intermediate | Advanced
    question_text = Column(Text, nullable=False)
    expected_answer = Column(Text, nullable=True)
    expected_concepts = Column(Text, nullable=True)  # JSON string list
    is_ai_generated = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    job_role = relationship("JobRole", back_populates="questions")
    answers = relationship("Answer", back_populates="question")
