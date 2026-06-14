"""Orchestrators: Supervisor graphs and dynamic factories.

LangGraph-first per AI-RULES.md.
"""

from .state import SerendipityState
from .supervisor_graph import build_demo_graph, build_serendipity_supervisor

__all__ = ["build_serendipity_supervisor", "build_demo_graph", "SerendipityState"]
