"""Serendipity Discoverer specialist implementation."""

from __future__ import annotations

from typing import Any

from .base import BaseSpecialist


class SerendipityDiscoverer(BaseSpecialist):
    name = "serendipity_discoverer"
    description = "Recombines signals into high-serendipity candidate ideas."

    def build(self, model: Any, **kwargs) -> Any:
        # In real use: create a StateGraph or use create_react_agent etc.
        # For supervisor, often we return pre-compiled agents.
        def discover(state: dict[str, Any]) -> dict[str, Any]:
            # Placeholder logic (replace with real tools + LLM calls)
            ideas = state.get("ideas", [])
            new_idea = f"Recombined-{len(ideas)} (serendipity: high)"
            return {"ideas": ideas + [new_idea], "last_specialist": self.name}

        # For demo we return a simple callable. Real impls return compiled graphs.
        discover.name = self.name  # some supervisor libs inspect .name
        return discover
