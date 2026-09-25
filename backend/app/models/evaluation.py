import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from sqlalchemy import Column, Integer, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    answer_id = Column(Integer, ForeignKey("answers.id"), unique=True, nullable=False)  # FK to answers (1-to-1)

    relevance_score = Column(Float, default=0.0)
    accuracy_score = Column(Float, default=0.0)
    completeness_score = Column(Float, default=0.0)
    similarity_score = Column(Float, default=0.0)
    communication_score = Column(Float, default=0.0)
    overall_score = Column(Float, default=0.0)

    feedback = Column(Text, nullable=True)
    strengths = Column(Text, nullable=True)    # JSON list
    improvements = Column(Text, nullable=True) # JSON list

    created_at = Column(DateTime, default=datetime.utcnow)

    answer = relationship("Answer", back_populates="evaluation")
