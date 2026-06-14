# AI-RULES.md - Strict Code Organization Commandments

## Purpose
Enforce architecture, boundaries, and standards for all code in this template and derived projects. Violations **must** be rejected in PRs. These rules exist to preserve separation of concerns, auditability, and the ability to maximize serendipity reliably in defense / low-resource settings.

## Core Principles
1. **Separation of Concerns**: Notebooks for exploration ONLY. All production code, agents, tools, and orchestration logic lives in `src/`.
2. **Modularity & Hierarchy**: Specialists defined via YAML packs (`agents/packs/`) + implementations in `src/serendipity_maximizer/agents/`. Orchestration (supervision, routing, conditionals) in `orchestrators/`.
3. **LangGraph Priority**: Dynamic multi-agent orchestration uses LangGraph (supervisor + conditional edges + state machines). Avoid ad-hoc scripts for agent coordination.
4. **Reproducibility & Audit**: Everything is config-driven, seeded, versioned, and checkpointed. IdeaRegister + checkpointers are mandatory for convergence and after-action review.
5. **Defense / SADIP Standards**: Low-SWaP configs by default. Explicit effort accounting in scoring. Metadata and provenance on all artifacts. Assurance level annotations.
6. **GitHub Architecture Standards**: Clean repo structure (CCDS base + AI extensions), good `.github/` workflows + templates, conventional PRs, no secrets in code.

## Directory Rules (Strict)
- `src/serendipity_maximizer/`: **Sole home** for importable production Python. Subdirectories:
  - `agents/`
  - `orchestrators/`
  - `discovery/` (recombination, scoring, registers)
  - `tools/`, `prompts/`, `utils/`, `config.py`
- `agents/`: YAML packs (`packs/`) + thin specialist registrations (`specialists/`). Heavy logic **never** here.
- `orchestrators/`: Supervisor graphs, factories, shared state (TypedDicts/Pydantic).
- `discovery/`: Pure(ish) functions + register classes. Usable from agents and (carefully) from exploration notebooks.
- `notebooks/`: Exploration, visualization, rapid prototyping **only**. Must never contain logic that should be in src. When stable, extract + delete.
- `data/`, `models/`, `reports/`, `references/`: Standard CCDS. Large/generated items are gitignored.
- **NEVER**:
  - Put agent logic, graphs, or tools in notebooks, root, `scripts/` (except thin runners), or mixed layers.
  - Hardcode prompts or routing in multiple places (centralize in packs + prompts/).
  - Skip type hints or Pydantic for config/state.

## Coding Standards
- Python 3.11+.
- Ruff (lint + format), mypy / type hints, Pydantic v2 for all config and state.
- Supervisor patterns: Hierarchical (supervisor → specialists), explicit tool-based or conditional handoff.
- All state changes go through LangGraph nodes / reducers for replayability.
- Config lives in `src/.../config.py` (and `agents/packs/*.yaml`). `.env` for secrets only.
- Every specialist must be buildable into a runnable / subgraph that the supervisor can hand off to.
- Add `metadata` with provenance, low_swap flags, assurance_level, version everywhere practical.

## LangGraph Patterns
- Primary entry: `build_serendipity_supervisor(...)` in `orchestrators/supervisor_graph.py`.
- Prefer `create_supervisor` from `langgraph-supervisor` for LLM-driven routing.
- Use explicit `add_conditional_edges` for deterministic / safety-critical paths (see demo graph).
- Always supply a checkpointer (MemorySaver at minimum; persistent in prod).
- State schema lives in `orchestrators/state.py` (extend SerendipityState carefully).

## PR & Backlog Rules
- All changes via PRs.
- Reference Project Maximizer backlog items / issues where applicable.
- AI-generated code must still obey these rules. The AI (or human reviewer) will flag violations.
- Update AI-RULES.md, README, and relevant packs when architecture changes.

## Violations
Violations break serendipity (by making recombination and scoring untrustworthy) and assurance (by destroying auditability).

When in doubt: put it in `src/serendipity_maximizer/`, make it config- or pack-driven, give it types + tests, and document the handoff.

---

This file is the single source of truth for architecture. Update it when the standards evolve.
