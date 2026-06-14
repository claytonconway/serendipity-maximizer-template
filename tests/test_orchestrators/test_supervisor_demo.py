"""Smoke tests for the demo supervisor (no LLM required)."""

from src.serendipity_maximizer.orchestrators.supervisor_graph import build_demo_graph


def test_demo_graph_runs_without_error(demo_state: dict):
    app = build_demo_graph()
    config = {"configurable": {"thread_id": "test-1"}}
    result = app.invoke(demo_state, config)
    assert isinstance(result, dict)
    # Demo path should have produced ideas and/or scores via conditionals
    assert "ideas" in result or "scored" in result


def test_demo_graph_has_expected_keys(demo_state: dict):
    app = build_demo_graph()
    config = {"configurable": {"thread_id": "test-2"}}
    result = app.invoke({**demo_state, "ideas": ["seed-idea"]}, config)
    assert "scored" in result or len(result.get("ideas", [])) > 0
