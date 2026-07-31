# Context engineering

The core skill of an **AI engineer** is not prompting — it is **designing what the agent sees**.

Models are stateless between sessions. Your job is to build **external memory and boundaries** the agent loads every time.

Official: [Customizing agents](https://cursor.com/learn/customizing-agents) · [Context](https://cursor.com/help/customization/context.md)

---

## The context stack (bottom → top)

```
┌─────────────────────────────────────────┐
│  Session: @files, chat spec, Plan doc   │  ← ephemeral, task-specific
├─────────────────────────────────────────┤
│  Skills (.cursor/skills/)               │  ← dynamic, scoped workflows
├─────────────────────────────────────────┤
│  AGENTS.md                              │  ← always-on project map
├─────────────────────────────────────────┤
│  LEARNINGS.md                           │  ← human + agent regression log
├─────────────────────────────────────────┤
│  Codebase + git history                 │  ← ground truth
└─────────────────────────────────────────┘
```

**Mobile dev habit:** "I know where everything is."  
**AI engineer habit:** "The agent knows because I **put it in AGENTS.md or a skill**."

---

## When to use what

| Need | Use |
|------|-----|
| "Always know our stack & verify ritual" | `AGENTS.md` |
| "When editing SwiftUI, use iOS 17 APIs" | Skill with `paths:` |
| "This one task needs these 3 files" | `@` in chat |
| "We failed this way twice" | LEARNINGS → promote to skill |
| "Multi-day feature" | Plan saved to `docs/plans/` |
| "Connect to GitHub / Jira / DB" | MCP (Week 3+) |

---

## Context engineering exercises (built into course)

| Exercise | Context skill |
|----------|---------------|
| 01–02 | `@` folder pin |
| 04, 06 | Extend AGENTS.md |
| 07 | `/create-skill` |
| 08 | Plan file in repo |
| 09 | AGENTS.md + skill on **your** non-mobile project |

---

## Good vs bad context

**Bad:** "Be smart about our codebase."  
**Good:** "Minimum iOS 17. Verify with Xcode ⌘B/⌘R. See `@HabitListView.swift` for list patterns."

**Bad:** 200-line AGENTS.md with every Swift rule.  
**Good:** 40-line AGENTS.md + `swiftui-exercises` skill scoped to `sample-app/`.

**Bad:** Copy entire files into chat every time.  
**Good:** `@path` + skill that points to canonical examples.

---

## Transfer beyond mobile

Same stack for:

- **Backend:** AGENTS.md with API conventions; skill for `paths: src/api/**`
- **Data:** skill for SQL/ETL verify steps
- **Content:** AGENTS.md + LEARNINGS (your That Guy / content OS pattern)
- **Telco:** domain truth tables in AGENTS.md or skill — agent implements, **you** own domain

The sandbox changes. **Context engineering does not.**

Next: [09-agents-md.md](09-agents-md.md) · [10-skills.md](10-skills.md)
