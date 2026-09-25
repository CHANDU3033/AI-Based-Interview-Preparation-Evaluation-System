import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Groq AI Engine — AI Interview System
=====================================
Handles:
  - Interview question generation
  - Answer evaluation with NLP scoring
  - Personalized feedback generation

Model: llama-3.1-8b-instant (free, ~0.5s response)
Falls back gracefully when API key is missing.
"""

import json
import logging
import re
from typing import Optional, List

logger = logging.getLogger(__name__)

_groq_client = None


def get_groq_client():
    """Singleton Groq client. Returns None if not configured."""
    global _groq_client
    if _groq_client is not None:
        return _groq_client
    try:
        from app.config import settings
        if not settings.GROQ_API_KEY:
            return None
        from groq import Groq
        _groq_client = Groq(api_key=settings.GROQ_API_KEY)
        logger.info("Groq AI client initialized.")
        return _groq_client
    except Exception as e:
        logger.error(f"Groq init failed: {e}")
        return None


def _call_groq(prompt: str, system: str = "", temperature: float = 0.2, max_tokens: int = 2048) -> Optional[str]:
    client = get_groq_client()
    if not client:
        return None
    try:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Groq API call failed: {e}")
        return None


def _extract_json(text: str):
    try:
        return json.loads(text)
    except Exception:
        pass
    match = re.search(r'```(?:json)?\s*(\{.*?\}|\[.*?\])\s*```', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            pass
    match = re.search(r'(\[.*\]|\{.*\})', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            pass
    return None


# ─── Question Generation ───────────────────────────────────────────────────────

def generate_interview_questions(
    role_name: str,
    difficulty: str,
    count: int = 5,
    previous_questions: List[str] = []
) -> Optional[List[dict]]:
    """
    Generate interview questions using Groq.
    Returns list of question dicts or None if unavailable.
    """
    prev_str = "\n".join(f"- {q}" for q in previous_questions[:10]) if previous_questions else "None"

    system = "You are an expert technical interviewer. Generate interview questions. Respond with valid JSON only. No explanations."

    prompt = f"""Generate {count} interview questions for a {role_name} position at {difficulty} level.

Previous questions already asked (do NOT repeat):
{prev_str}

Return a JSON array exactly like this:
[
  {{
    "question_text": "Explain the difference between a list and a tuple in Python.",
    "category": "Technical",
    "difficulty": "{difficulty}",
    "expected_answer": "A list is mutable while a tuple is immutable...",
    "expected_concepts": ["mutable", "immutable", "list", "tuple", "performance"]
  }}
]

Rules:
- category must be one of: Technical, HR, Project, Scenario
- Mix categories: mostly Technical, 1-2 HR
- difficulty: {difficulty}
- Make questions specific to {role_name}
- expected_concepts: 3-6 key concepts the answer should mention

JSON array:"""

    response = _call_groq(prompt, system)
    if not response:
        return None
    result = _extract_json(response)
    if isinstance(result, list):
        logger.info(f"Groq generated {len(result)} questions for {role_name}")
        return result
    return None


# ─── Answer Evaluation ─────────────────────────────────────────────────────────

def evaluate_interview_answer(
    question_text: str,
    expected_answer: str,
    expected_concepts: List[str],
    student_answer: str
) -> Optional[dict]:
    """
    Evaluate a student's answer using Groq.
    Returns evaluation dict with scores and feedback.
    """
    concepts_str = ", ".join(expected_concepts) if expected_concepts else "N/A"

    system = "You are an expert interview evaluator. Evaluate answers objectively. Respond with valid JSON only."

    prompt = f"""Evaluate this interview answer and provide scores.

QUESTION: {question_text}

EXPECTED ANSWER: {expected_answer or 'Not provided'}

KEY CONCEPTS EXPECTED: {concepts_str}

STUDENT ANSWER: {student_answer}

Provide this exact JSON:
{{
  "relevance_score": 85,
  "accuracy_score": 78,
  "completeness_score": 72,
  "similarity_score": 80,
  "communication_score": 88,
  "overall_score": 81,
  "feedback": "Good understanding of the core concept. You correctly identified mutability as the key difference. Consider also mentioning performance implications and use cases.",
  "strengths": ["Correctly identified mutability", "Clear explanation", "Good use of examples"],
  "improvements": ["Mention performance implications", "Discuss when to use each", "Add more specific examples"]
}}

Scoring rules:
- All scores: 0-100 integers
- relevance_score: how relevant the answer is to the question
- accuracy_score: technical correctness
- completeness_score: how many expected concepts were covered
- similarity_score: semantic similarity to expected answer
- communication_score: clarity, structure, and coherence
- overall_score: weighted average (accuracy 30%, relevance 25%, completeness 20%, similarity 15%, communication 10%)
- feedback: 2-3 specific, constructive sentences
- strengths: 2-3 things the student did well
- improvements: 2-3 specific areas to improve

JSON:"""

    response = _call_groq(prompt, system)
    if not response:
        return None
    result = _extract_json(response)
    if result and "overall_score" in result:
        logger.info(f"Groq evaluated answer: {result.get('overall_score')}%")
        return result
    return None


# ─── Feedback Generation ───────────────────────────────────────────────────────

def generate_interview_feedback(
    role_name: str,
    scores: dict,
    weak_areas: List[str],
    strong_areas: List[str]
) -> Optional[dict]:
    """Generate personalized feedback and recommendations after interview."""
    prompt = f"""Generate personalized interview feedback for a {role_name} candidate.

Scores: {json.dumps(scores)}
Strong Areas: {', '.join(strong_areas) if strong_areas else 'None identified'}
Weak Areas: {', '.join(weak_areas) if weak_areas else 'None identified'}

Return this JSON:
{{
  "overall_feedback": "2-3 sentence overall assessment",
  "recommendations": ["Topic 1 to study", "Topic 2 to practice", "Topic 3 to review"],
  "learning_plan": ["Step 1: ...", "Step 2: ...", "Step 3: ..."]
}}

JSON:"""

    response = _call_groq(prompt)
    if not response:
        return None
    return _extract_json(response)


def is_groq_available() -> bool:
    return get_groq_client() is not None
