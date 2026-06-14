# AI-RULES.md - Strict Code Organization Commandments

## Purpose
Enforce architecture, boundaries, and standards for all code in this template and derived projects. Violations must be rejected in PRs.

## Core Principles
1. **Separation of Concerns**: Notebooks for exploration ONLY. Production code in src/.
2. **Modularity**: Agents in agents/, orchestrators in src/orchestrators/, etc.
3. **LangGraph Priority**: Use LangGraph for supervisor patterns where dynamic orchestration is needed.
4. **Reproducibility**: Config-driven, seeded, versioned.
5. **Defense Standards**: Low-SWaP configs, assurance, auditability.

## Directory Rules
- **src/serendipity_maximizer/**: Core package. Subdirs: agents/, orchestrators/, etc. No business logic outside.
- **agents/**: YAML packs and specialist implementations.
- **orchestrators/**: Supervisor graphs, dynamic factories.
- **discovery/**: Recombination, registers, scoring.
- **NEVER**: Put agent logic in notebooks, root, or mixed layers.

## Coding Standards
- Python 3.11+, Ruff lint, type hints, Pydantic configs.
- Supervisor patterns: Hierarchical, tool-based handoff.
- All changes via PRs with Project Maximizer backlog.

Violations break serendipity and assurance.