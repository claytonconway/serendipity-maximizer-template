"""Thin wrapper for Impact x Serendipity scorer."""
from __future__ import annotations

from typing import Any


def get_impact_scorer_runnable(model: Any = None):
    def _score(state: dict) -> dict:
        cands = state.get("candidates", [])
        scored = []
        for c in cands:
            scored.append({"idea": c, "score": 0.42})  # placeholder
        return {"scored": scored}

    return _score
