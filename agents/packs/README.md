# Agent Packs

Place declarative YAML/JSON definitions here.

Each pack should declare:
- name, role, stage
- description
- tools it may call
- handoff conditions (used to inform supervisor prompt or custom routing)
- system_prompt_ref (path under prompts/ or inline)
- config (low-swap budgets, thresholds, etc.)
- metadata (version, assurance_level, domain)

The supervisor and factory will eventually load these to assemble the team dynamically.
