"""Placeholder metric functions for relevance and factuality.

Implementations are intentionally simple; replace with advanced models or
embedding-based similarity as the project matures.
"""
from __future__ import annotations
from typing import Sequence
import math


def relevance_score(reference_terms: Sequence[str], answer: str) -> float:
    """Compute naive relevance as fraction of reference terms present in answer.

    Args:
        reference_terms: Keywords expected in a good answer.
        answer: Generated answer text.
    Returns:
        Float in [0,1].
    """
    if not reference_terms:
        return 0.0
    lower_answer = answer.lower()
    hits = sum(1 for t in reference_terms if t.lower() in lower_answer)
    return hits / len(reference_terms)


def factuality_placeholder(context: str, answer: str) -> float:
    """Very naive factuality heuristic using token overlap Jaccard index.

    Args:
        context: Retrieved or source context.
        answer: Generated answer.
    Returns:
        Float in [0,1].
    """
    ctx_tokens = set(context.lower().split())
    ans_tokens = set(answer.lower().split())
    if not ctx_tokens or not ans_tokens:
        return 0.0
    intersection = ctx_tokens & ans_tokens
    union = ctx_tokens | ans_tokens
    return len(intersection) / len(union)


if __name__ == "__main__":  # Basic smoke tests
    rel = relevance_score(["python", "embedding"],
                          "This covers Python embedding tricks")
    fact = factuality_placeholder(
        "python embedding retrieval", "Python embedding tricks retrieval")
    print({"relevance": rel, "factuality": fact})
