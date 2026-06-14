"""Thin wrapper / registration for the Serendipity Discoverer specialist.

In production this would construct a full LangGraph agent or tool-calling runnable
from the pack + prompts + tools defined under src/.
"""
from __future__ import annotations

from typing import Any


def get_serendipity_discoverer_runnable(model: Any = None):
    """Return a runnable (or compiled subgraph) for the discoverer.

    Placeholder until full impl in src/serendipity_maximizer/agents/.
    """
    # TODO: build from pack + state + tools
    def _discover(state: dict) -> dict:
        return {"candidates": state.get("candidates", []) + ["[DISCOVERED PLACEHOLDER]"]}

    return _discover
