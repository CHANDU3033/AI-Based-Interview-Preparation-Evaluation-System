import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Resume Router — AI Interview System
Handles PDF/TXT resume uploads and parsing for personalized interview questions.
"""
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from typing import Optional
from app.utils.resume_parser import extract_text_from_pdf, parse_resume_content
from app.models.user import User
from app.utils.auth import get_current_user

router = APIRouter(prefix="/resume", tags=["Resume Parsing"])


@router.post("/parse")
async def parse_resume(
    file: Optional[UploadFile] = File(None),
    raw_text: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
):
    """
    Parse an uploaded PDF resume or raw text resume.
    Extracts key skills, project mentions, and suggests matching job roles.
    """
    resume_text = ""

    if file:
        file_bytes = await file.read()
        if file.filename.lower().endswith(".pdf"):
            resume_text = extract_text_from_pdf(file_bytes)
        else:
            try:
                resume_text = file_bytes.decode("utf-8", errors="ignore")
            except Exception:
                resume_text = ""

    if not resume_text and raw_text:
        resume_text = raw_text

    if not resume_text:
        raise HTTPException(status_code=400, detail="Please upload a valid PDF file or paste resume text.")

    result = parse_resume_content(resume_text)
    return result
