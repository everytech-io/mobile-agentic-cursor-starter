# AGENTS.md — full guide

Official: [Rules / AGENTS.md](https://cursor.com/docs/rules#agentsmd)

`AGENTS.md` is the **simplest always-on instruction file** for Cursor Agent. No YAML. Plain markdown at the repo root (or nested in subfolders).

## Why it exists

Agents do not remember last session. `AGENTS.md` is onboarding doc for the agent — same idea as onboarding a junior dev.

This repo's live example: [AGENTS.md](../AGENTS.md)

## What belongs in AGENTS.md

| Include | Example |
|---------|---------|
| Stack + deployment target | iOS 17, SwiftUI (sandbox) |
| Folder map | where sample app, docs, exercises live |
| Commands | named verify commands: `pytest`, `npm test`, `xcodebuild`, `curl …` |
| Workflow rules | parallel verify after edits ([14-verification-practices.md](14-verification-practices.md)) |
| Intentional gaps | do not "fix" exercise gaps early |
| Out of scope | no new packages without exercise |

## What does NOT belong

- Entire style guides (use SwiftLint)
- Every git command (agent knows git)
- Secrets or API keys
- Long copied code (point to canonical files with `@`)

Keep it **under ~80 lines**. If it grows, split conventions into a **skill**.

## Nested AGENTS.md

Cursor merges nested files when you work in subfolders:

```
project/
  AGENTS.md              # global
  sample-app/
    AGENTS.md            # iOS-specific (optional)
```

More specific wins on conflict. For this course, root `AGENTS.md` is enough.

## AGENTS.md vs skills vs rules

| | AGENTS.md | Skills | Rules (`.mdc`) |
|---|-----------|--------|----------------|
| Format | Plain markdown | `SKILL.md` + frontmatter | `.mdc` + frontmatter |
| When loaded | Always (root) | When relevant / `/skill` | Always or glob-scoped |
| Best for | Project map, workflow | Domain workflows, conventions | Org compliance |

**Teaching order:** AGENTS.md first → skills when patterns repeat → rules only if compliance requires always-on.

## Exercise

[Exercise 06 — Extend AGENTS.md](../exercises/06-agents-md.md)

## Template (copy to your app)

```markdown
# Project instructions for Cursor Agent

## Stack
- Platform: your stack (backend, script, mobile sandbox, etc.)
- Verify: name commands in this file — tests, lint, curl, build. Run human + agent review in parallel.

## Layout
- `src/` — app code
- `tests/` — automated verifiers

## Rules
- Match existing architecture in @main module file
- No new dependencies without asking
- Parallel verify before hand-back (automated + human diff + review)

## Out of scope
- Backend / CI changes unless ticket says so
```

Next: [10-skills.md](10-skills.md)
