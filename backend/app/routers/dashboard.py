import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models.user import User
from app.models.interview import Interview
from app.utils.auth import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def get_dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Stats: total interviews, avg score, best score, recent interviews."""
    interviews = (
        db.query(Interview)
        .filter(Interview.user_id == current_user.id, Interview.status == "COMPLETED")
        .order_by(Interview.completed_at.desc())
        .all()
    )

    total = len(interviews)
    avg_score = round(sum(iv.overall_score for iv in interviews if iv.overall_score) / total, 1) if total else 0
    best_score = max((iv.overall_score for iv in interviews if iv.overall_score), default=0)

    recent = [
        {
            "id": iv.id,
            "role_name": iv.role_name,
            "difficulty": iv.difficulty,
            "overall_score": iv.overall_score,
            "status": iv.status,
            "completed_at": iv.completed_at,
        }
        for iv in interviews[:3]
    ]

    return {
        "total_interviews": total,
        "avg_score": avg_score,
        "best_score": best_score,
        "recent_interviews": recent,
    }


@router.get("/progress")
def get_score_progression(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Score progression over time for line chart."""
    interviews = (
        db.query(Interview)
        .filter(Interview.user_id == current_user.id, Interview.status == "COMPLETED")
        .order_by(Interview.completed_at.asc())
        .all()
    )

    return [
        {
            "interview_number": i + 1,
            "role_name": iv.role_name,
            "overall_score": iv.overall_score,
            "date": iv.completed_at.strftime("%d %b") if iv.completed_at else "",
        }
        for i, iv in enumerate(interviews)
    ]


@router.get("/weak-topics")
def get_weak_topics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Aggregate weak areas across all interviews."""
    interviews = (
        db.query(Interview)
        .filter(Interview.user_id == current_user.id, Interview.status == "COMPLETED")
        .all()
    )

    weak_counts = {}
    for iv in interviews:
        if iv.weak_areas:
            areas = json.loads(iv.weak_areas)
            for area in areas:
                weak_counts[area] = weak_counts.get(area, 0) + 1

    # Sort by frequency
    sorted_weak = sorted(weak_counts.items(), key=lambda x: x[1], reverse=True)
    return {"weak_topics": [{"topic": k, "count": v} for k, v in sorted_weak[:5]]}


@router.get("/recommendations")
def get_recommendations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Personalized study recommendations based on interview performance."""
    interviews = (
        db.query(Interview)
        .filter(Interview.user_id == current_user.id, Interview.status == "COMPLETED")
        .order_by(Interview.completed_at.desc())
        .limit(5)
        .all()
    )

    all_recs = []
    seen = set()
    for iv in interviews:
        if iv.recommendations:
            recs = json.loads(iv.recommendations)
            for r in recs:
                if r not in seen:
                    all_recs.append(r)
                    seen.add(r)

    if not all_recs:
        all_recs = [
            "Practice Python fundamentals daily",
            "Review SQL JOIN types and window functions",
            "Work on structuring your answers clearly",
            "Study ML algorithms and their use cases",
        ]

    # Score breakdown from latest interview
    score_breakdown = {}
    if interviews:
        iv = interviews[0]
        score_breakdown = {
            "Technical Knowledge": iv.technical_score or 0,
            "Answer Relevance": iv.relevance_score or 0,
            "Completeness": iv.completeness_score or 0,
            "Communication": iv.communication_score or 0,
        }

    return {
        "recommendations": all_recs[:6],
        "score_breakdown": score_breakdown,
    }
