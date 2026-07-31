# Exercise 04 — Capture learning (+ optional skill)

**Goal:** Make the workflow durable across sessions.  
**Time:** ~45 minutes  
**Read first:** [docs/04-rules-and-context.md](../docs/04-rules-and-context.md)

## Part A — LEARNINGS audit

1. Open [LEARNINGS.md](../LEARNINGS.md)
2. Ensure you have at least **2 dated entries** from exercises 01–03
3. Add a third entry summarizing your biggest surprise so far

Template:

```markdown
## YYYY-MM-DD — Week 1 reflection
- Biggest surprise about Agent:
- Biggest surprise about Xcode verify:
- One thing I'll always do from now on:
```

## Part B — Optional: add a skill (not rules)

You do **not** need `.cursor/rules/` for this course. Use:

- **AGENTS.md** — always-on project context (already in repo)
- **Skills** — load when editing Swift files (see `.cursor/skills/swiftui-exercises/`)

If Agent made the same mistake twice, ask:

```
/create-skill

When editing SwiftUI under sample-app/, never use NavigationView.
Remind me to verify in Xcode after edits.
```

Review the generated skill before keeping it.

## Part C — Optional commit

If you're learning git + Agent:

```
Stage only LEARNINGS.md. Write a one-line commit message. Do not push.
```

## Done when

- [ ] LEARNINGS.md has 3+ entries
- [ ] You understand AGENTS.md vs skills vs LEARNINGS
- [ ] You know you can skip `.cursor/rules/` unless you need always-on team guardrails

Course complete for Week 1 core — see [docs/07-week-1-syllabus.md](../docs/07-week-1-syllabus.md).
