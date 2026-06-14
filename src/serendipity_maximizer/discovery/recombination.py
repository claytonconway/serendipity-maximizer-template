"""Recombination engine for generating novel combinations of ideas/signals."""

from __future__ import annotations

import random
from typing import Any


def recombine(
    signals: list[str],
    budget: int = 12,
    seed: int = 42,
) -> list[dict[str, Any]]:
    """Generate recombinant ideas from input signals.

    This is a placeholder. Real version would use embeddings, LLMs, or
    structured matrices for cross-domain analogies.
    """
    random.seed(seed)
    ideas = []
    for i in range(min(budget, len(signals) * 2)):
        combo = random.sample(signals, k=min(2, len(signals)))
        ideas.append(
            {
                "id": f"REC-{i}",
                "recombination": " x ".join(combo),
                "novelty": round(random.uniform(0.5, 0.98), 2),
            }
        )
    return ideas
