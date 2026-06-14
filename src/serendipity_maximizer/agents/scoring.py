"""Impact x Serendipity / Effort scoring specialist."""

from __future__ import annotations

from typing import Any

from .base import BaseSpecialist


class ImpactScorer(BaseSpecialist):
    name = "impact_scorer"
    description = "Scores candidates using (Impact * Serendipity) / Effort with Low-SWaP filters."

    def build(self, model: Any, **kwargs) -> Any:
        def score(state: dict[str, Any]) -> dict[str, Any]:
            ideas = state.get("ideas", [])
            scored = []
            for i, idea in enumerate(ideas):
                # Placeholder formula
                s = {
                    "idea": idea,
                    "impact": 0.8,
                    "serendipity": 0.75,
                    "effort": 0.3,
                    "final_score": round((0.8 * 0.75) / 0.3, 3),
                }
                scored.append(s)
            return {"scored": scored, "last_specialist": self.name}

        score.name = self.name
        return score
