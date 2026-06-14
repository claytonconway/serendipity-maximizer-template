"""LangGraph Supervisor for Serendipity Maximizer.

Implements hierarchical supervisor pattern using langgraph-supervisor.
Supports:
- Dynamic routing to specialists (discovery, scoring, mapping, convergence)
- Configurable handoff / conditional behavior via prompt + specialist metadata
- Memory checkpointer for replay / audit
- Low-SWaP friendly construction

Conditionals: The supervisor model itself decides routing (via tool-calling handoff).
Additional conditional edges or post-routing logic can be added in wrappers here.
"""

from __future__ import annotations

from typing import Any

from langgraph.checkpoint.memory import MemorySaver
from langgraph_supervisor import create_supervisor

from ..agents.scoring import ImpactScorer
from ..agents.serendipity import SerendipityDiscoverer
from .state import SerendipityState


def build_serendipity_supervisor(
    agents: list[Any] | None = None,
    model: Any = None,
    prompt: str | None = None,
    checkpointer: Any = None,
) -> Any:
    """Build the main compiled supervisor graph.

    Args:
        agents: Specialist callables/graphs (with .name attr preferred).
                If None, builds demo specialists.
        model: LLM or chat model compatible with the supervisor (e.g. ChatOpenAI).
               For pure demo without keys, pass None and a no-op supervisor is used.
        prompt: Custom system prompt for the supervisor router.
        checkpointer: Optional checkpointer. Defaults to in-memory.

    Returns:
        Compiled LangGraph app (runnable).
    """
    if agents is None:
        # Build default demo specialists (callables with .name attached)
        agents = [
            SerendipityDiscoverer().build(model),
            ImpactScorer().build(model),
        ]

    system_prompt = prompt or (
        "You are the Serendipity Supervisor. "
        "Route dynamically for recombination (discovery), "
        "scoring (Impact x Serendipity / Effort + low-swap), SBIR mapping, and convergence. "
        "Consider auditability and Low-SWaP. Decide next route or converge."
    )

    if model is None:
        # Demo / stub mode: no real LLM supervisor. Return a simple sequential simulator.
        return _build_demo_supervisor(agents)

    workflow = create_supervisor(
        agents,
        model=model,
        prompt=system_prompt,
        # Add more supervisor config here as langgraph-supervisor evolves (e.g. handoff tools)
    )

    if checkpointer is None:
        checkpointer = MemorySaver()

    return workflow.compile(checkpointer=checkpointer)


def _build_demo_supervisor(agents: list[Any]) -> Any:
    """Fallback demo supervisor when no model is provided.

    Simulates routing in a deterministic order for quick validation of the template
    without requiring API keys. Useful for CI, local smoke tests, and phone-based exploration.
    """
    from langgraph.graph import END, StateGraph

    # Build a tiny state graph that runs agents in a sensible discovery -> score order
    builder = StateGraph(SerendipityState)

    def supervisor_router(state: SerendipityState) -> str:
        # Simple conditional routing logic (example of explicit conditionals)
        ideas = state.get("ideas", [])
        scored = state.get("scored", [])
        if not ideas:
            return "serendipity_discoverer"
        if not scored:
            return "impact_scorer"
        return "END"

    def run_discoverer(state: SerendipityState) -> SerendipityState:
        for agent in agents:
            if getattr(agent, "name", None) == "serendipity_discoverer":
                return agent(state)  # type: ignore
        # fallback
        return {**state, "ideas": state.get("ideas", []) + ["[demo-idea-from-fallback]"]}

    def run_scorer(state: SerendipityState) -> SerendipityState:
        for agent in agents:
            if getattr(agent, "name", None) == "impact_scorer":
                return agent(state)  # type: ignore
        scored = [{"idea": i, "final_score": 0.5} for i in state.get("ideas", [])]
        return {**state, "scored": scored}

    builder.add_node("serendipity_discoverer", run_discoverer)
    builder.add_node("impact_scorer", run_scorer)

    builder.set_entry_point("serendipity_discoverer")

    # Conditional edges demonstrate explicit conditionals (in addition to supervisor LLM routing)
    builder.add_conditional_edges(
        "serendipity_discoverer",
        supervisor_router,
        {
            "serendipity_discoverer": "serendipity_discoverer",
            "impact_scorer": "impact_scorer",
            "END": END,
        },
    )
    builder.add_conditional_edges(
        "impact_scorer",
        supervisor_router,
        {
            "serendipity_discoverer": "serendipity_discoverer",
            "impact_scorer": "impact_scorer",
            "END": END,
        },
    )

    # For demo we attach checkpointer but require thread_id on invoke (standard LangGraph)
    graph = builder.compile(checkpointer=MemorySaver())
    return graph


def build_demo_graph() -> Any:
    """Convenience for quick runnable demo graph (no LLM required)."""
    return build_serendipity_supervisor(agents=None, model=None)


if __name__ == "__main__":
    """Run a minimal end-to-end demo when invoked as module.

    python -m serendipity_maximizer.orchestrators.supervisor_graph
    """
    print("=== Serendipity Maximizer Supervisor Demo (no LLM keys needed) ===\n")

    app = build_demo_graph()

    # Initial seed state
    initial_state: SerendipityState = {
        "messages": [],
        "ideas": [],
        "scored": [],
        "task": "Maximize serendipity around dual-use low-SWaP sensing for maritime awareness",
        "metadata": {"low_swap": True, "budget": 5},
    }

    # Invoke with thread config (required when checkpointer is present)
    config = {"configurable": {"thread_id": "demo-main"}}
    result = app.invoke(initial_state, config)

    print("Final state keys:", list(result.keys()))
    print("\nDiscovered ideas:", result.get("ideas", []))
    print("\nScored ideas:", result.get("scored", []))
    print("\nDemo complete. Extend specialists + wire real model for production runs.")
    print("See Makefile target 'run-serendipity' and agents/packs/ for configuration.")
