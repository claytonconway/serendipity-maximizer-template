"""Pydantic configuration for Serendipity Maximizer.

Emphasizes Low-SWaP, reproducibility, auditability, and defense constraints.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class LowSwapConfig(BaseModel):
    """Low Size, Weight, and Power constraints."""

    max_tokens_per_step: int = Field(2048, description="Token budget per specialist step")
    max_parallel_agents: int = Field(3, description="Concurrency limit for supervisor")
    use_quantized: bool = Field(True)
    prefer_local: bool = Field(False)


class SerendipityConfig(BaseModel):
    """Core application config."""

    project: str = "serendipity-maximizer"
    env: Literal["dev", "staging", "prod"] = "dev"
    low_swap: LowSwapConfig = Field(default_factory=LowSwapConfig)
    recombination_budget: int = 50
    scoring_formula: str = "(impact * serendipity) / effort"
    audit_enabled: bool = True
    seed: int = 42

    model_config = {"env_prefix": "SERENDIPITY_", "extra": "ignore"}


def get_config() -> SerendipityConfig:
    """Factory for loaded config. Extend with pydantic-settings or dotenv later."""
    return SerendipityConfig()
