import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Resume Parser Utility — AI Interview System
Extracts text from PDF/TXT resumes and identifies technical skills, experience keywords, and domain relevance.
"""
import io
import re
import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

SKILL_BANK = [
    "Python", "Java", "C++", "C#", "JavaScript", "TypeScript", "HTML", "CSS", "SQL",
    "React", "Node.js", "Express", "FastAPI", "Flask", "Django", "Vue.js", "Angular",
    "Machine Learning", "Deep Learning", "Artificial Intelligence", "Data Science",
    "NLP", "Natural Language Processing", "Computer Vision", "TensorFlow", "PyTorch",
    "scikit-learn", "Pandas", "NumPy", "Matplotlib", "Seaborn", "PostgreSQL", "MySQL",
    "MongoDB", "SQLite", "Redis", "Docker", "Kubernetes", "AWS", "Azure", "GCP",
    "Git", "GitHub", "Linux", "REST API", "Microservices", "Data Structures", "Algorithms"
]


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract clean text content from PDF file bytes."""
    try:
        import pypdf
        reader = pypdf.PdfReader(io.BytesIO(file_bytes))
        text_parts = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text_parts.append(t)
        return "\n".join(text_parts)
    except Exception as e:
        logger.error(f"Failed to extract PDF text: {e}")
        try:
            return file_bytes.decode('utf-8', errors='ignore')
        except Exception:
            return ""


def parse_resume_content(resume_text: str) -> Dict[str, Any]:
    """Parse resume text to detect skills, project mentions, and suggested role."""
    if not resume_text:
        return {
            "extracted_text": "",
            "detected_skills": [],
            "suggested_role": "Software Developer",
            "detected_projects": 0,
            "summary": "No text content detected in resume."
        }

    clean_text = resume_text.strip()
    text_lower = clean_text.lower()

    detected_skills = []
    for skill in SKILL_BANK:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            detected_skills.append(skill)

    projects_count = len(re.findall(r'\b(project|projects|built|developed|implemented)\b', text_lower))

    suggested_role = "Software Developer"
    ai_skills = {"Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "NLP", "Data Science"}
    data_skills = {"SQL", "Pandas", "NumPy", "Data Analysis", "PostgreSQL", "MySQL"}
    python_skills = {"Python", "FastAPI", "Django", "Flask"}

    detected_set = set(detected_skills)
    if len(detected_set.intersection(ai_skills)) >= 2:
        suggested_role = "AI/ML Engineer"
    elif len(detected_set.intersection(data_skills)) >= 2:
        suggested_role = "Data Analyst"
    elif "SQL" in detected_set and len(detected_set) <= 3:
        suggested_role = "SQL Developer"
    elif len(detected_set.intersection(python_skills)) >= 1:
        suggested_role = "Python Developer"

    return {
        "extracted_text": clean_text[:2000],
        "detected_skills": detected_skills,
        "suggested_role": suggested_role,
        "detected_projects": projects_count,
        "summary": f"Detected {len(detected_skills)} key technical skills ({', '.join(detected_skills[:5])})."
    }
