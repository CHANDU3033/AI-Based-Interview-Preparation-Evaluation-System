import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    interview_id = Column(Integer, ForeignKey("interviews.id"), nullable=False)   # FK to interviews
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)    # FK to questions
    question_text = Column(Text, nullable=False)     # denormalized for reports
    answer_text = Column(Text, nullable=False)
    audio_path = Column(String(255), nullable=True)
    duration_seconds = Column(Integer, nullable=True)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    interview = relationship("Interview", back_populates="answers")
    question = relationship("Question", back_populates="answers")
    evaluation = relationship("Evaluation", back_populates="answer", uselist=False, cascade="all, delete-orphan")
