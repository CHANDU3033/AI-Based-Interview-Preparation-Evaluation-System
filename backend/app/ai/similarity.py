import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
"""
Text Similarity & Speech Analysis Utilities
============================================
Uses TF-IDF cosine similarity (scikit-learn) as a lightweight
NLP fallback when Groq is unavailable.
"""

import re
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FILLER_WORDS = [
    "umm", "uh", "um", "like", "you know", "actually",
    "basically", "literally", "sort of", "kind of", "right",
    "so", "well", "okay", "anyway"
]


def calculate_similarity(text1: str, text2: str) -> float:
    """
    Compute TF-IDF cosine similarity between two texts.
    Returns a float between 0.0 and 1.0.
    """
    if not text1 or not text2:
        return 0.0
    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf = vectorizer.fit_transform([text1, text2])
        score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return round(float(score), 4)
    except Exception:
        return 0.0


def count_filler_words(text: str) -> Dict:
    """Count filler word occurrences in text."""
    text_lower = text.lower()
    counts = {}
    total = 0
    for word in FILLER_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        count = len(re.findall(pattern, text_lower))
        if count > 0:
            counts[word] = count
            total += count
    return {"total": total, "words": counts}


def calculate_wpm(text: str, duration_seconds: int) -> float:
    """Calculate words per minute from text and duration."""
    if not text or duration_seconds <= 0:
        return 0.0
    word_count = len(text.split())
    return round((word_count / duration_seconds) * 60, 1)


def extract_keywords(text: str, top_n: int = 10) -> List[str]:
    """Extract top keywords using TF-IDF on single document."""
    if not text:
        return []
    try:
        vectorizer = TfidfVectorizer(stop_words="english", max_features=top_n)
        vectorizer.fit_transform([text])
        return list(vectorizer.get_feature_names_out())
    except Exception:
        return []


def check_concepts_covered(text: str, concepts: List[str]) -> Dict:
    """Check which expected concepts appear in the student's answer."""
    text_lower = text.lower()
    covered = []
    missing = []
    for concept in concepts:
        if concept.lower() in text_lower:
            covered.append(concept)
        else:
            missing.append(concept)
    coverage = len(covered) / len(concepts) if concepts else 0.0
    return {
        "covered": covered,
        "missing": missing,
        "coverage_ratio": round(coverage, 2)
    }
