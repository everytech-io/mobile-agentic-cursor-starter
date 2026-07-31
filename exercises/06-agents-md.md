# Exercise 06 — AGENTS.md verify ritual

**Goal:** Document Release Ready verifiers in AGENTS.md.  
**Read first:** [docs/09-agents-md.md](../docs/09-agents-md.md), [docs/14-verification-practices.md](../docs/14-verification-practices.md)

Add **## Verify ritual** to [AGENTS.md](../AGENTS.md):

```markdown
## Verify ritual

After release-ready/ edits (parallel):
1. Automated: `cd release-ready && ./scripts/verify.sh`
2. Human: read diff + done-when path
3. Agent: /review-bugbot on release-ready/
4. LEARNINGS.md if surprised
```

## Done when

- [ ] AGENTS.md lists named commands
- [ ] New Agent chat reminds you to verify without re-prompting

Next: [07-create-skill.md](07-create-skill.md)
