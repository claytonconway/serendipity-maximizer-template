"""Pure scoring functions (Impact * Serendipity / Effort).

Can be used by agents or directly in notebooks (for exploration only).
"""

from __future__ import annotations

from typing import Any


def score_idea(
    impact: float,
    serendipity: float,
    effort: float,
    low_swap_penalty: float = 1.0,
) -> float:
    """Compute the primary serendipity score.

    Higher is better. Apply low_swap_penalty (0-1) to down-rank high-resource ideas.
    """
    if effort <= 0:
        effort = 0.01
    raw = (impact * serendipity) / effort
    return round(raw * low_swap_penalty, 4)


def rank_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Rank a list of scored candidate dicts."""
    return sorted(
        candidates,
        key=lambda c: c.get("final_score", 0.0),
        reverse=True,
    )
