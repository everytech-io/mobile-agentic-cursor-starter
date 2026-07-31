# Exercise 07 — Create a skill

**Goal:** `/create-skill` for Release Ready workflow.  
**Read first:** [docs/10-skills.md](../docs/10-skills.md)

Extend or duplicate [.cursor/skills/release-ready-core/SKILL.md](../.cursor/skills/release-ready-core/SKILL.md):

```
/create-skill

Name: release-ready-core (or my-release-ready)
Description: Release Ready Python conventions + parallel verify after edits.
Paths: release-ready/**/*.py

Include: exercise gaps, pytest verify, /review-bugbot parallel, no FastAPI in core.
```

Test: `/release-ready-core` in new Agent chat after editing `store.py`.

Next: [08-full-loop.md](08-full-loop.md)
