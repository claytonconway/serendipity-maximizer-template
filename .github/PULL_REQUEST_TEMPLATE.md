## Summary
<!-- One paragraph describing the change. Reference backlog item if applicable. -->

## Type of Change
- [ ] New feature / specialist
- [ ] Bug fix
- [ ] Refactor (must not change behavior)
- [ ] Docs / template improvement
- [ ] Architecture / AI-RULES change (high scrutiny)

## AI-RULES Compliance Checklist
- [ ] All new production code is under `src/serendipity_maximizer/`
- [ ] No agent/orchestration logic added to notebooks or root
- [ ] YAML packs or config updated if routing / specialists changed
- [ ] Types + tests added/updated
- [ ] State / handoff changes documented in state.py or AI-RULES if needed

## Testing
- [ ] Existing tests pass (`make test`)
- [ ] Demo runs (`make run-serendipity`)
- [ ] Added unit tests for new modules

## Low-SWaP / Assurance Impact
<!-- Describe any changes to resource usage, auditability, or scoring. -->

## Related
- Backlog item: 
- Related PRs: 
