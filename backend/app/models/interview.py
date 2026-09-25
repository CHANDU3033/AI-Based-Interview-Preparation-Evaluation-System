import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)          # FK to users
    role_id = Column(Integer, ForeignKey("job_roles.id"), nullable=False)          # FK to job_roles
    role_name = Column(String(100), nullable=False)    # denormalized
    difficulty = Column(String(20), nullable=False)    # Beginner | Intermediate | Advanced
    mode = Column(String(10), default="TEXT")          # TEXT | VOICE
    total_questions = Column(Integer, default=10)
    question_ids = Column(Text, nullable=True)         # JSON list of question IDs for this session
    questions_answered = Column(Integer, default=0)

    # Aggregate scores (filled on completion)
    overall_score = Column(Float, nullable=True)
    technical_score = Column(Float, nullable=True)
    relevance_score = Column(Float, nullable=True)
    completeness_score = Column(Float, nullable=True)
    communication_score = Column(Float, nullable=True)

    status = Column(String(20), default="IN_PROGRESS")  # IN_PROGRESS | COMPLETED | CANCELLED
    strong_areas = Column(Text, nullable=True)           # JSON list
    weak_areas = Column(Text, nullable=True)             # JSON list
    recommendations = Column(Text, nullable=True)        # JSON list

    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="interviews")
    answers = relationship("Answer", back_populates="interview", cascade="all, delete-orphan")
