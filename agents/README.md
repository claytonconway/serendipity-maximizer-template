# Agents

Top-level agents directory per AI-RULES.md.

## Layout
- `packs/`: Declarative YAML/JSON agent definitions, prompts, tools registration, routing hints. Used for configuration-driven specialists and for cookiecutter templating.
- `specialists/`: Thin Python implementations or entrypoints for specialists. Heavy logic belongs in `src/serendipity_maximizer/agents/`.

## Usage
YAML packs define:
- role
- stage (e.g. discovery, scoring, mapping, convergence)
- capabilities
- prompt templates (refs)
- handoff conditions for supervisor

The supervisor (LangGraph) loads these for dynamic routing + tool use.
