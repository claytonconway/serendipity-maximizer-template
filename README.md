# Serendipity-Maximizer-Template

Extended [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) (CCDS) template for **multi-agent orchestration with LangGraph**, tailored for the Serendipity Maximizer and SADIP platform.

## Purpose
Maximize serendipitous discovery of high-impact, low-effort ideas (especially dual-use / defense) through structured recombination, rigorous scoring (Impact × Serendipity / Effort), and supervisor-orchestrated specialist agents.

## Key Features
- **LangGraph-first** supervisor pattern with explicit conditional routing + handoffs.
- **Strict architecture** enforced by [AI-RULES.md](AI-RULES.md).
- **YAML-driven specialists** (packs in `agents/packs/`) for configuration and audit.
- **First-class discovery/scoring** modules + idea register for reproducibility and assurance.
- Low-SWaP, auditability, and defense-oriented defaults.
- Full CCDS structure (data/, notebooks exploration-only, reports, etc.) + GitHub repo standards.

## Directory Structure (Extended CCDS + Multi-Agent)

```
.
├── agents/                    # YAML packs + thin specialist registrations (see AI-RULES)
│   ├── packs/
│   │   ├── serendipity_discoverer.yaml
│   │   ├── impact_scorer.yaml
│   │   ├── sbir_mapper.yaml
│   │   └── convergence_agent.yaml
│   └── specialists/
├── config/                    # Low-swap, env, assurance configs
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── external/
├── docs/
├── models/                    # Artifacts (gitignored)
├── notebooks/                 # Exploration ONLY (port to src/ when stable)
│   └── exploration/
├── references/
├── reports/
│   └── figures/
├── scripts/
├── src/serendipity_maximizer/
│   ├── agents/                # Real specialist implementations (BaseSpecialist, etc.)
│   ├── orchestrators/         # Supervisor graphs, factory, state
│   ├── discovery/             # Recombination, scoring, register
│   ├── tools/
│   ├── prompts/
│   └── utils/
├── tests/
├── .github/                   # Workflows, PR/issue templates (GitHub architecture standards)
├── AI-RULES.md                # Strict code organization commandments (enforced)
├── cookiecutter.json          # Use as cookiecutter template source
├── Makefile
├── pyproject.toml
└── README.md
```

## Quickstart

```bash
# 1. Install (editable)
make install
# or: pip install -e .

# 2. (Optional) Dev tools + LLM providers
make dev-install

# 3. Run the supervisor demo (no API keys required!)
make run-serendipity
# or: python -m serendipity_maximizer.orchestrators.supervisor_graph
```

For real LLMs:
- Copy `.env.example` → `.env` and add keys.
- Pass a real `model` (ChatOpenAI etc.) to `build_serendipity_supervisor`.

## Running with real agents + supervisor routing

See:
- `src/serendipity_maximizer/orchestrators/supervisor_graph.py`
- `src/serendipity_maximizer/orchestrators/state.py`
- `agents/packs/*.yaml` + `src/.../agents/`

Extend the demo specialists or wire full tool-calling agents.

## Development Standards
- Follow **AI-RULES.md** religiously. PRs violating boundaries will be rejected.
- Python 3.11+, Ruff + type hints.
- All production logic in `src/`. Notebooks = exploration only.
- Changes via PRs referencing Project Maximizer backlog items (when applicable).

## SADIP / Defense Orientation
- Low-SWaP configs (see `config.py` and packs).
- Emphasis on audit (checkpointers, registers, metadata).
- SBIR mapping specialists and dual-use awareness built into routing.

## Next Steps / TODOs (from template)
- Wire real LLM model + tools (Tavily, SBIR APIs, vector stores).
- Persistent checkpointer (Postgres/SQLite via LangGraph).
- Full agent pack loader in `orchestrators/factory.py`.
- Data ingestion pipelines.
- Evaluation harness for serendipity quality.

See `Makefile` for additional targets.

Use this template for all new Serendipity Maximizer / SADIP-related AI projects.
