# Exercise 09 — AI engineer graduation (non-mobile)

**Goal:** Prove the agentic loop on **real work outside StarterApp**.  
**Time:** ~2–3 hours  
**Read first:** [docs/12-ai-engineer-competencies.md](../docs/12-ai-engineer-competencies.md)

This is the transition from "mobile dev who used Cursor" to **AI engineer**.

---

## Pick ONE task (not SwiftUI)

Choose work you actually have — one bounded outcome:

| Option | Example done-when |
|--------|-------------------|
| **A. Script / CLI** | Python/shell script that automates one repetitive task; runs clean |
| **B. API / backend** | One endpoint or handler change + test or curl verify |
| **C. Docs / spec** | PRD or RFC from messy notes; saved in repo |
| **D. Ticket closure** | Jira/Linear ticket → branch → fix → PR description |
| **E. MCP workflow** | Wire one MCP (GitHub, etc.); agent completes one read-only query you specify |

Open **that project's folder** in Cursor (or a dedicated branch). Copy pattern from this repo:

- `AGENTS.md` (adapted)
- `.cursor/skills/` (at least one skill)
- `LEARNINGS.md` (start fresh or append)

---

## Required loop (all steps)

| Step | Requirement |
|------|-------------|
| 1. SPEC | Written done-when / out-of-scope in chat or markdown |
| 2. CONTEXT | AGENTS.md + `@` relevant files **or** one skill |
| 3. PLAN | Plan Mode for anything >1 file; save to `docs/plans/` |
| 4. DELEGATE | Agent implements; you review every diff |
| 5. VERIFY | **Non-Xcode verifier:** tests, curl, script run, linter, manual checklist |
| 6. REVIEW | `/review-bugbot` or explicit review prompt |
| 7. CAPTURE | LEARNINGS entry + skill update if agent repeated a mistake |

---

## Plan prompt template

```
Plan Mode:

Project: <your repo — NOT StarterApp>
Task: <A–E above>

Done when:
- [ ] Verifier: <test command / curl / script / human checklist>
- [ ] Diff scoped to task only
- [ ] AGENTS.md updated if new convention discovered

Out of scope: ...

Save plan to workspace when approved.
@AGENTS.md
```

---

## Mentor rubric (Level 3 AI engineer)

- [ ] Task was **not** StarterApp UI
- [ ] Spec had testable done-when
- [ ] Verification evidence exists (command output, test pass, PR link)
- [ ] AGENTS.md or skill exists in target project
- [ ] Can explain **context stack** from [13-context-engineering.md](../docs/13-context-engineering.md) without notes

---

## Optional Week 4+

- MCP server for a tool your team uses
- Cloud Agent for long-running research branch
- Subagent: planner (Fable) + executor split
- Port `ios-verify` pattern → `backend-verify` skill

You are no longer learning Cursor for mobile. You are **operating as an AI engineer**.
