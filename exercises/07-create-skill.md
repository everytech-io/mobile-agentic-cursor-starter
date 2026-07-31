# Exercise 07 — Create a skill

**Goal:** `/create-skill` for ShipGate workflow.  
**Read first:** [docs/10-skills.md](../docs/10-skills.md)

Extend or duplicate [.cursor/skills/shipgate-core/SKILL.md](../.cursor/skills/shipgate-core/SKILL.md):

```
/create-skill

Name: shipgate-core (or my-shipgate)
Description: ShipGate Python conventions + parallel verify after edits.
Paths: shipgate/**/*.py

Include: exercise gaps, pytest verify, /review-bugbot parallel, no FastAPI in core.
```

Test: `/shipgate-core` in new Agent chat after editing `store.py`.

Next: [08-full-loop.md](08-full-loop.md)
