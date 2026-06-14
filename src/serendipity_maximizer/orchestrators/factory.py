"""Dynamic supervisor / agent factory.

Supports role-stage matrices and config-driven assembly from packs.
"""

from __future__ import annotations

from typing import Any

from .supervisor_graph import build_serendipity_supervisor


def create_serendipity_supervisor_from_packs(
    packs_dir: str = "agents/packs",
    model: Any = None,
    **kwargs,
) -> Any:
    """Example factory that could load YAML packs and instantiate specialists.

    Currently delegates to the main builder (extend as needed).
    """
    # Future: load packs, build specialists via registry, then pass list to supervisor.
    return build_serendipity_supervisor(agents=[], model=model, **kwargs)
