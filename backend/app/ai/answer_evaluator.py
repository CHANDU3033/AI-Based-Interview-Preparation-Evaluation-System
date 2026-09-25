import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Answer Evaluation Engine
=========================
Primary:  Groq LLM evaluation (semantic, nuanced)
Fallback: TF-IDF cosine similarity + concept keyword matching
"""

import json
import logging
from typing import List, Optional

from app.ai.groq_engine import evaluate_interview_answer as groq_evaluate, is_groq_available
from app.ai.similarity import calculate_similarity, check_concepts_covered

logger = logging.getLogger(__name__)


def evaluate_answer(
    question_text: str,
    expected_answer: str,
    expected_concepts: List[str],
    student_answer: str,
    duration_seconds: Optional[int] = None,
) -> dict:
    """
    Evaluate a student's answer.
    Tries Groq first; falls back to TF-IDF + concept matching.
    Returns a full evaluation dict.
    """
    if not student_answer or not student_answer.strip():
        return _empty_evaluation("No answer provided.")

    # Try Groq LLM evaluation
    if is_groq_available():
        result = groq_evaluate(question_text, expected_answer, expected_concepts, student_answer)
        if result:
            # Ensure strengths/improvements are lists
            result["strengths"] = result.get("strengths") or []
            result["improvements"] = result.get("improvements") or []
            return result

    # Fallback: rule-based NLP evaluation
    logger.info("Groq unavailable — using fallback NLP evaluation")
    return _fallback_evaluation(question_text, expected_answer, expected_concepts, student_answer)


def _fallback_evaluation(
    question_text: str,
    expected_answer: str,
    expected_concepts: List[str],
    student_answer: str,
) -> dict:
    """TF-IDF + keyword-concept fallback evaluator."""
    # Semantic similarity to expected answer
    sim = calculate_similarity(expected_answer or question_text, student_answer)
    similarity_score = round(sim * 100)

    # Concept coverage
    concept_result = check_concepts_covered(student_answer, expected_concepts)
    coverage = concept_result["coverage_ratio"]
    completeness_score = round(coverage * 100)

    # Relevance: similarity to question
    relevance_sim = calculate_similarity(question_text, student_answer)
    relevance_score = round(min(relevance_sim * 130, 100))  # slight boost

    # Accuracy: based on similarity + concept coverage
    accuracy_score = round((similarity_score * 0.6 + completeness_score * 0.4))

    # Communication: based on answer length and structure
    word_count = len(student_answer.split())
    if word_count < 10:
        communication_score = 30
    elif word_count < 30:
        communication_score = 55
    elif word_count < 80:
        communication_score = 70
    else:
        communication_score = min(85, 60 + word_count // 10)

    # Overall weighted
    overall_score = round(
        accuracy_score * 0.30 +
        relevance_score * 0.25 +
        completeness_score * 0.20 +
        similarity_score * 0.15 +
        communication_score * 0.10
    )

    # Generate feedback
    covered = concept_result["covered"]
    missing = concept_result["missing"]

    strengths = []
    improvements = []

    if relevance_score >= 70:
        strengths.append("Answer is relevant to the question")
    if covered:
        strengths.append(f"Covered key concepts: {', '.join(covered[:3])}")
    if word_count >= 50:
        strengths.append("Provided a detailed response")

    if missing:
        improvements.append(f"Mention these key concepts: {', '.join(missing[:3])}")
    if similarity_score < 60:
        improvements.append("Review the expected answer concepts more thoroughly")
    if word_count < 30:
        improvements.append("Provide more detailed and elaborated answers")

    if not strengths:
        strengths = ["Attempted to answer the question"]
    if not improvements:
        improvements = ["Continue practicing for more depth"]

    feedback = (
        f"Your answer scored {overall_score}% overall. "
        f"{'You covered ' + str(len(covered)) + ' of ' + str(len(expected_concepts)) + ' key concepts. ' if expected_concepts else ''}"
        f"{'Focus on: ' + ', '.join(missing[:2]) + '.' if missing else 'Good concept coverage!'}"
    )

    return {
        "relevance_score": relevance_score,
        "accuracy_score": accuracy_score,
        "completeness_score": completeness_score,
        "similarity_score": similarity_score,
        "communication_score": communication_score,
        "overall_score": overall_score,
        "feedback": feedback,
        "strengths": strengths,
        "improvements": improvements,
    }


def _empty_evaluation(reason: str) -> dict:
    return {
        "relevance_score": 0.0,
        "accuracy_score": 0.0,
        "completeness_score": 0.0,
        "similarity_score": 0.0,
        "communication_score": 0.0,
        "overall_score": 0.0,
        "feedback": reason,
        "strengths": [],
        "improvements": ["Please provide an answer to receive evaluation."],
    }
