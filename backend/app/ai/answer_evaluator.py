import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Answer Evaluation Engine — Generous Student Scoring
===================================================
Applies student-friendly scoring policy:
Any intermediate or reasonable answer attempt receives up to ~70%+ performance scores
across Overall, Technical Accuracy, Relevance, Completeness, and Communication metrics.
Textbook verbatim accuracy is NOT required.
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
    Applies generous evaluation: intermediate/attempted answers receive ~68%-75%+ scores.
    """
    if not student_answer or len(student_answer.strip().split()) < 2:
        return _empty_evaluation("No meaningful answer provided.")

    # Try Groq LLM evaluation if available
    if is_groq_available():
        result = groq_evaluate(question_text, expected_answer, expected_concepts, student_answer)
        if result:
            result["strengths"] = result.get("strengths") or []
            result["improvements"] = result.get("improvements") or []

            # Ensure intermediate answers get generous 70%+ scoring boost
            for key in ["overall_score", "accuracy_score", "relevance_score", "completeness_score", "communication_score"]:
                if key in result and isinstance(result[key], (int, float)):
                    if result[key] > 0 and result[key] < 68:
                        result[key] = round(68 + (result[key] / 68) * 7) # boost up to 70-75%
            return result

    # Fallback: student-friendly NLP evaluation
    return _generous_nlp_evaluation(question_text, expected_answer, expected_concepts, student_answer)


def _generous_nlp_evaluation(
    question_text: str,
    expected_answer: str,
    expected_concepts: List[str],
    student_answer: str,
) -> dict:
    """Generous student-friendly NLP evaluator awarding up to 70%+ for intermediate answers."""
    words = student_answer.strip().split()
    word_count = len(words)

    # Calculate raw NLP similarity & concept coverage
    sim = calculate_similarity(expected_answer or question_text, student_answer)
    concept_result = check_concepts_covered(student_answer, expected_concepts)
    coverage = concept_result["coverage_ratio"]
    relevance_sim = calculate_similarity(question_text, student_answer)

    # 1. Relevance: Baseline 70% for any valid answer attempt, boosted up to 95%
    relevance_score = round(min(70 + (relevance_sim * 25), 95))

    # 2. Technical Accuracy: Baseline 68% for intermediate attempt, boosted by concepts & similarity
    accuracy_boost = (sim * 15) + (coverage * 15)
    accuracy_score = round(min(68 + accuracy_boost, 96))

    # 3. Completeness: Baseline 66% + concept coverage boost up to 92%
    completeness_score = round(min(66 + (coverage * 26), 95))

    # 4. Communication: Based on answer structure (Baseline 70% for standard attempt)
    if word_count < 5:
        communication_score = 60
    elif word_count < 15:
        communication_score = 70
    elif word_count < 40:
        communication_score = 78
    else:
        communication_score = min(92, 75 + (word_count // 10))

    # 5. Overall Weighted Score (Generous intermediate target ~70-75%)
    overall_score = round(
        accuracy_score * 0.35 +
        relevance_score * 0.25 +
        completeness_score * 0.20 +
        communication_score * 0.20
    )
    overall_score = max(68, min(overall_score, 98))

    # Generate constructive feedback
    covered = concept_result["covered"]
    missing = concept_result["missing"]

    strengths = [
        "Good effort explaining the core technical concepts",
        "Answer is relevant to the interview question"
    ]
    if covered:
        strengths.append(f"Demonstrated understanding of: {', '.join(covered[:3])}")
    if word_count >= 25:
        strengths.append("Provided a well-structured response")

    improvements = []
    if missing:
        improvements.append(f"To reach 85%+, include details on: {', '.join(missing[:3])}")
    if word_count < 20:
        improvements.append("Elaborate further with real-world examples or code syntax")
    if not improvements:
        improvements.append("Keep practicing advanced scenarios for top score")

    feedback = (
        f"Solid intermediate response! You scored {overall_score}% overall. "
        f"{'Key concepts covered: ' + ', '.join(covered[:2]) + '. ' if covered else ''}"
        f"Keep building on your technical explanations to reach advanced mastery!"
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
