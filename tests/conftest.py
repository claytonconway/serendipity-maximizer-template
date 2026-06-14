"""Pytest configuration and shared fixtures for Serendipity Maximizer tests."""

import pytest

from src.serendipity_maximizer.config import SerendipityConfig, get_config


@pytest.fixture
def serendipity_config() -> SerendipityConfig:
    return get_config()


@pytest.fixture
def demo_state():
    return {
        "messages": [],
        "ideas": [],
        "scored": [],
        "task": "Test task for serendipity",
        "metadata": {"low_swap": True},
    }
