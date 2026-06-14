"""Idea register for persistence, versioning, and auditability."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class IdeaRecord:
    id: str
    content: str
    score: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    created: str = field(default_factory=lambda: datetime.utcnow().isoformat())


class IdeaRegister:
    """In-memory (or DB-backed) register of discovered ideas.

    Supports audit, replay, and convergence.
    """

    def __init__(self):
        self._store: dict[str, IdeaRecord] = {}

    def add(self, record: IdeaRecord) -> None:
        self._store[record.id] = record

    def get(self, idea_id: str) -> IdeaRecord | None:
        return self._store.get(idea_id)

    def top_k(self, k: int = 5) -> list[IdeaRecord]:
        return sorted(
            self._store.values(),
            key=lambda r: r.score or 0.0,
            reverse=True,
        )[:k]

    def all(self) -> list[IdeaRecord]:
        return list(self._store.values())
