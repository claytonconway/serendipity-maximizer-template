"""Base specialist agent interface.

All specialists should be LangGraph-compatible (callable runnables or compiled StateGraphs)
so they can be passed to langgraph_supervisor.create_supervisor.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseSpecialist(ABC):
    """Abstract base for specialists.

    Specialists are typically thin wrappers that return a compiled subgraph or
    a tool-calling agent bound to a specific role/stage.
    """

    name: str
    description: str

    @abstractmethod
    def build(self, model: Any, **kwargs) -> Any:
        """Return a runnable or compiled graph for this specialist."""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.name}>"
