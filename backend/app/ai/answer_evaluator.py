import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Answer Evaluation Engine — Student Friendly 60% to 70% Intermediate Policy
========================================================================
Applies calibrated scoring policy:
Intermediate level answer attempts receive 60% to 70% performance scores
across Overall, Technical Accuracy, Relevance, Completeness, and Communication metrics.
Textbook exact answers are not expected for intermediate grades.
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
    Applies calibrated evaluation: intermediate attempts receive 60% to 70% scores.
    """
    if not student_answer or len(student_answer.strip().split()) < 2:
        return _empty_evaluation("No meaningful answer provided.")

    # Try Groq LLM evaluation if available
    if is_groq_available():
        result = groq_evaluate(question_text, expected_answer, expected_concepts, student_answer)
        if result:
            result["strengths"] = result.get("strengths") or []
            result["improvements"] = result.get("improvements") or []

            # Calibrate intermediate scores to 60-70% range
            for key in ["overall_score", "accuracy_score", "relevance_score", "completeness_score", "communication_score"]:
                if key in result and isinstance(result[key], (int, float)):
                    if 0 < result[key] < 75:
                        result[key] = round(60 + (result[key] / 75) * 10, 1) # scale into 60-70% range
            return result

    # Fallback: student-friendly NLP evaluation
    return _intermediate_60_70_nlp_evaluation(question_text, expected_answer, expected_concepts, student_answer)


def _intermediate_60_70_nlp_evaluation(
    question_text: str,
    expected_answer: str,
    expected_concepts: List[str],
    student_answer: str,
) -> dict:
    """NLP evaluator placing intermediate attempts in 60% to 70% performance range."""
    words = student_answer.strip().split()
    word_count = len(words)

    # Calculate raw NLP similarity & concept coverage
    sim = calculate_similarity(expected_answer or question_text, student_answer)
    concept_result = check_concepts_covered(student_answer, expected_concepts)
    coverage = concept_result["coverage_ratio"]
    relevance_sim = calculate_similarity(question_text, student_answer)

    # 1. Relevance: Baseline 62% for valid answer attempt, capped at 70% for intermediate
    relevance_score = round(min(62 + (relevance_sim * 8), 70), 1)

    # 2. Technical Accuracy: Baseline 60% for intermediate attempt, capped at 70%
    accuracy_boost = (sim * 5) + (coverage * 5)
    accuracy_score = round(min(60 + accuracy_boost, 70), 1)

    # 3. Completeness: Baseline 60% + concept coverage boost up to 70%
    completeness_score = round(min(60 + (coverage * 10), 70), 1)

    # 4. Communication: Baseline 62% for standard attempt, up to 70%
    if word_count < 5:
        communication_score = 55.0
    elif word_count < 15:
        communication_score = 62.0
    elif word_count < 40:
        communication_score = 66.0
    else:
        communication_score = min(70.0, 65.0 + (word_count // 10))

    # 5. Overall Weighted Score (Strictly calibrated inside 60% - 70% for intermediate attempts)
    overall_score = round(
        accuracy_score * 0.35 +
        relevance_score * 0.25 +
        completeness_score * 0.20 +
        communication_score * 0.20,
        1
    )
    overall_score = max(60.0, min(overall_score, 70.0))

    # Generate constructive feedback
    covered = concept_result["covered"]
    missing = concept_result["missing"]

    strengths = [
        "Good intermediate effort explaining key concepts",
        "Answer is relevant to the question topic"
    ]
    if covered:
        strengths.append(f"Demonstrated concept understanding: {', '.join(covered[:3])}")
    if word_count >= 20:
        strengths.append("Provided a clear response")

    improvements = []
    if missing:
        improvements.append(f"To reach 80%+, include details on: {', '.join(missing[:3])}")
    if word_count < 25:
        improvements.append("Provide further elaboration and code/syntax examples")
    if not improvements:
        improvements.append("Keep practicing advanced technical topics for higher scores")

    feedback = (
        f"Intermediate performance! You scored {overall_score}% overall. "
        f"{'Key concepts covered: ' + ', '.join(covered[:2]) + '. ' if covered else ''}"
        f"Continue refining your technical explanations to reach advanced levels!"
    )

    return {
        "relevance_score": float(relevance_score),
        "accuracy_score": float(accuracy_score),
        "completeness_score": float(completeness_score),
        "similarity_score": round(sim * 100, 1),
        "communication_score": float(communication_score),
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
