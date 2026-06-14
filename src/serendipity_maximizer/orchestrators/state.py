"""Shared state schemas for the Serendipity Maximizer supervisor and specialists.

Use TypedDict or Pydantic for LangGraph state.
"""

from __future__ import annotations

from typing import Annotated, Any, TypedDict

from langgraph.graph.message import add_messages


class SerendipityState(TypedDict, total=False):
    """Primary state passed between supervisor and specialists."""

    messages: Annotated[list[dict[str, Any]], add_messages]
    ideas: list[str]  # raw or recombined ideas
    scored: list[dict[str, Any]]  # ideas + scores
    register: dict[str, Any]  # serialized IdeaRegister snapshot
    last_specialist: str | None
    task: str  # high-level user task / seed query
    metadata: dict[str, Any]  # low_swap flags, budgets, provenance, etc.
