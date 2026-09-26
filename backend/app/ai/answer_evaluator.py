import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Answer Evaluation Engine - Dynamic Semantic AI Evaluator with Echo and Junk Filter
===================================================================================
Rules:
1. Candidate repeating/copying the question text as the answer = 0% Score.
2. Junk/nonsense/unrelated text = 0% Score.
3. Realistic semantic AI evaluation based on accuracy, relevance, completeness, and communication.
"""

import json
import logging
import re
from typing import List, Optional

from app.ai.groq_engine import evaluate_interview_answer as groq_evaluate, is_groq_available
from app.ai.similarity import calculate_similarity, check_concepts_covered

logger = logging.getLogger(__name__)


def is_question_echo(question_text: str, student_answer: str) -> bool:
    """Detect if student merely repeated or copied the question text."""
    q_clean = re.sub(r'[^a-zA-Z0-9\s]', '', question_text.lower()).strip()
    a_clean = re.sub(r'[^a-zA-Z0-9\s]', '', student_answer.lower()).strip()

    if q_clean == a_clean:
        return True

    stop_words = {"what", "is", "are", "how", "why", "explain", "the", "a", "an", "and", "or", "in", "of", "to", "for", "with", "between", "difference", "does", "your"}
    q_words = set(q_clean.split()) - stop_words
    a_words = set(a_clean.split()) - stop_words

    if not a_words:
        return True

    # If answer contains NO new keywords beyond the question keywords
    if a_words.issubset(q_words):
        return True

    return False


def evaluate_answer(
    question_text: str,
    expected_answer: str,
    expected_concepts: List[str],
    student_answer: str,
    duration_seconds: Optional[int] = None,
) -> dict:
    """Evaluate student answer with strict echo and junk detection."""
    if not student_answer or len(student_answer.strip().split()) < 1:
        return _empty_evaluation("No answer provided.")

    # 1. Detect if candidate repeated the question text
    if is_question_echo(question_text, student_answer):
        return {
            "relevance_score": 0.0,
            "accuracy_score": 0.0,
            "completeness_score": 0.0,
            "similarity_score": 0.0,
            "communication_score": 0.0,
            "overall_score": 0.0,
            "feedback": "You repeated the question text instead of providing an answer. Please explain the technical concept in your own words.",
            "strengths": [],
            "improvements": ["Do not repeat the question text", "Provide a real explanation for the technical topic"],
        }

    # Try Groq LLM evaluation if available
    if is_groq_available():
        result = groq_evaluate(question_text, expected_answer, expected_concepts, student_answer)
        if result:
            result["strengths"] = result.get("strengths") or []
            result["improvements"] = result.get("improvements") or []
            return result

    # Fallback: Robust NLP evaluation
    return _calibrated_nlp_evaluation(question_text, expected_answer, expected_concepts, student_answer)


def _calibrated_nlp_evaluation(
    question_text: str,
    expected_answer: str,
    expected_concepts: List[str],
    student_answer: str,
) -> dict:
    """Dynamic NLP evaluator enforcing 0% for junk/echo and realistic continuous scoring."""
    words = student_answer.strip().split()
    word_count = len(words)

    # Calculate NLP similarity and concept coverage
    sim = calculate_similarity(expected_answer or question_text, student_answer)
    concept_result = check_concepts_covered(student_answer, expected_concepts)
    coverage = concept_result["coverage_ratio"]
    relevance_sim = calculate_similarity(question_text, student_answer)

    # 2. Detect junk / nonsense / zero-relevance answers
    if sim < 0.08 and coverage == 0 and relevance_sim < 0.15:
        return {
            "relevance_score": 0.0,
            "accuracy_score": 0.0,
            "completeness_score": 0.0,
            "similarity_score": 0.0,
            "communication_score": 0.0,
            "overall_score": 0.0,
            "feedback": "Your answer does not appear to be relevant to the technical topic. Please provide a relevant technical response.",
            "strengths": [],
            "improvements": ["Focus on the specific technical subject", "Include relevant core terminology"],
        }

    # Dynamic continuous score calculation based on semantic NLP and concept coverage
    accuracy_score = round(min(100.0, max(0.0, (sim * 55.0) + (coverage * 45.0))), 1)
    relevance_score = round(min(100.0, max(0.0, (relevance_sim * 40.0) + (sim * 60.0))), 1)
    
    length_factor = min(1.0, word_count / 25.0)
    completeness_score = round(min(100.0, max(0.0, (coverage * 65.0) + (length_factor * 35.0))), 1)
    
    comm_base = min(95.0, 50.0 + (word_count * 1.5))
    communication_score = round(min(100.0, max(0.0, comm_base)), 1)

    overall_score = round(
        (accuracy_score * 0.35) + 
        (relevance_score * 0.25) + 
        (completeness_score * 0.20) + 
        (communication_score * 0.20), 1
    )

    covered = concept_result["covered"]
    missing = concept_result["missing"]

    strengths = []
    if relevance_score >= 50:
        strengths.append("Answer is relevant to the question topic")
    if covered:
        strengths.append(f"Demonstrated concept understanding: {', '.join(covered[:3])}")
    if word_count >= 15:
        strengths.append("Provided a structured response")

    improvements = []
    if missing:
        improvements.append(f"To improve your score, include: {', '.join(missing[:3])}")
    if word_count < 25:
        improvements.append("Provide further elaboration and code/syntax examples")

    feedback = (
        f"Evaluation completed. You scored {overall_score}% overall. "
        f"{'Key concepts covered: ' + ', '.join(covered[:2]) + '. ' if covered else ''}"
        f"Keep practicing to expand your technical depth!"
    )

    return {
        "relevance_score": float(relevance_score),
        "accuracy_score": float(accuracy_score),
        "completeness_score": float(completeness_score),
        "similarity_score": round(sim * 100, 1),
        "communication_score": float(communication_score),
        "overall_score": float(communication_score),
        "overall_score": float(overall_score),
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
        "improvements": ["Please provide a detailed response to receive evaluation."],
    }
