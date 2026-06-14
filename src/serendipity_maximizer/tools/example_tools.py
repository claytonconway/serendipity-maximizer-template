"""Example tool stubs.

In real usage, implement using @tool from langchain_core.tools or langgraph tools.
Register in specialists or pass to agent builders.
"""

from __future__ import annotations


def dummy_retriever(query: str) -> list[str]:
    """Placeholder for reference / vector retrieval."""
    return [f"[REF] signal related to: {query}", "[REF] cross-domain analogy candidate"]


def dummy_scorer(idea: str) -> dict:
    """Placeholder calculator."""
    return {"idea": idea, "impact": 0.7, "serendipity": 0.65, "effort": 0.25}
