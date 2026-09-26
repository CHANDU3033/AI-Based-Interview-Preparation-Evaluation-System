import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
import logging
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_tables, SessionLocal
from app.routers import auth, questions, interviews, evaluations, dashboard, resume
from app.ai.groq_engine import is_groq_available
from app.ui import get_ui_html

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Interview Preparation & Evaluation System",
    description="AI-powered mock interview platform for students. Conducts personalized interviews, evaluates answers with NLP, and generates detailed performance reports.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ─── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Standalone Web UI Routes ──────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/ui", response_class=HTMLResponse, include_in_schema=False)
def get_standalone_ui():
    """Serves the complete single-page Web Application interface directly from FastAPI with strict no-cache headers."""
    headers = {
        "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
        "Pragma": "no-cache",
        "Expires": "0"
    }
    return HTMLResponse(content=get_ui_html(), headers=headers)

# ─── Routers ───────────────────────────────────────────────────────────────────
app.include_router(auth.router,          prefix="/api")
app.include_router(questions.router,     prefix="/api")
app.include_router(interviews.router,    prefix="/api")
app.include_router(evaluations.router,   prefix="/api")
app.include_router(dashboard.router,     prefix="/api")
app.include_router(resume.router,        prefix="/api")


# ─── Startup ───────────────────────────────────────────────────────────────────
@app.on_event("startup")
def startup_event():
    create_tables()
    logger.info("Database tables created")

    # Auto-seed if empty
    db = SessionLocal()
    try:
        from app.models.question import JobRole
        if db.query(JobRole).count() == 0:
            logger.info("Seeding database with question bank...")
            import seed_data
            seed_data.seed_database()
    except Exception as e:
        logger.error(f"Auto-seed failed: {e}")
    finally:
        db.close()

    groq_status = "Groq AI enabled" if is_groq_available() else "Groq not configured (fallback NLP active)"
    logger.info(groq_status)
    logger.info("AI Interview System started successfully!")


# ─── Health Check ──────────────────────────────────────────────────────────────
@app.get("/health", tags=["Health"])
def health_check():
    from app.models.user import User
    from app.models.question import JobRole, Question
    from app.models.interview import Interview

    db = SessionLocal()
    try:
        users = db.query(User).count()
        roles = db.query(JobRole).count()
        questions = db.query(Question).count()
        total_interviews = db.query(Interview).count()
        db_status = "connected"
    except Exception as e:
        users = roles = questions = total_interviews = 0
        db_status = f"error: {str(e)}"
    finally:
        db.close()

    return {
        "status": "ok",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "database": {
            "status": db_status,
            "users": users,
            "job_roles": roles,
            "questions": questions,
            "total_interviews": total_interviews,
        },
        "features": {
            "groq_ai": is_groq_available(),
            "text_interview": True,
            "nlp_evaluation": True,
            "voice_interview": True,  # Phase 2
        },
    }
