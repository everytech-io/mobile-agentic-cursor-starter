# The shift: mobile developer → AI engineer

This course uses **StarterApp** (SwiftUI) as a sandbox. The goal is **not** to make you a faster iOS coder.

The goal is to make you an **AI engineer** — someone who directs agents, owns specs, builds durable context, and verifies outcomes like production systems depend on it.

Mobile is where you already have judgment (simulator, App Store, UX). We borrow that discipline and apply it to **agentic work everywhere**.

---

## Two identities

| Mobile dev (old default) | AI engineer (where you're going) |
|--------------------------|----------------------------------|
| "I write the screen" | "I write the spec and verify the outcome" |
| Success = compiles + looks right | Success = **correct behavior under verification** |
| Context in my head | Context in **AGENTS.md, skills, plans, LEARNINGS** |
| AI = autocomplete | AI = **agent with tools** you delegate to |
| Review = code review | Review = **diff + runtime + review agent** |
| Ship = TestFlight | Ship = **prompt → plan → implement → verify → capture** |

You are not becoming a "prompt engineer." You are becoming someone who **operates agent systems** the way you once operated Xcode.

---

## What an AI engineer actually does

1. **Writes specs agents can execute** — goal, done-when, out-of-scope (not vibes)
2. **Engineers context** — AGENTS.md, skills, `@` pins, saved plans in git
3. **Routes work to the right mode** — Ask / Plan / Agent / Debug / review ([08-cursor-modes.md](08-cursor-modes.md))
4. **Verifies like ops** — cheap checks first, expensive agent second, **human gate before trust**
5. **Captures learnings** — agents forget; **LEARNINGS.md and skills** don't
6. **Closes the loop** — spec → plan → code → verify → ticket/deploy ([user's security arc pattern](https://cursor.com/learn/creating-features))
7. **Knows domain beats model** — the agent doesn't know your BSS, your QBS index, your SwiftUI deployment target; **you do**

StarterApp is **Week 1 gym equipment**. Week 3+ is your real codebase, APIs, scripts, and agent workflows.

---

## The AI engineer loop (memorize this)

```
SPEC → CONTEXT → [PLAN] → DELEGATE (agent) → VERIFY → REVIEW → CAPTURE → REPEAT
```

| Step | Artifact |
|------|----------|
| SPEC | Done-when checklist in chat or markdown |
| CONTEXT | AGENTS.md + skills + `@files` |
| PLAN | Plan Mode output in `docs/plans/` |
| DELEGATE | Agent / subagent / MCP tool |
| VERIFY | Xcode, tests, lint, logs — **evidence** |
| REVIEW | `/review-bugbot`, agent review |
| CAPTURE | LEARNINGS.md → skill when pattern repeats |

---

## Three-week arc (this program)

| Week | You become capable of… | Sandbox |
|------|------------------------|---------|
| **1** | Agent loop + verify discipline | StarterApp + Xcode |
| **2** | Modes, AGENTS.md, skills, Debug, review | Same app, richer agent ops |
| **3** | **Transfer** — same loop on *your* work | Your repo / API / script / ticket |

Week 3 is where "AI engineer" becomes real. See [12-ai-engineer-competencies.md](12-ai-engineer-competencies.md) and [Exercise 09](../exercises/09-ai-engineer-graduation.md).

---

## What this is NOT

- Not "vibe coding" mobile UI
- Not replacing Swift/Kotlin learning
- Not MCP/agent-framework hype on day one
- Not skipping verification because the agent said "done"

---

## Read next

1. [00-watch-first.md](00-watch-first.md) — Cursor Learn (agents foundation)
2. [00-start-here.md](00-start-here.md) — Day 1 mechanics
3. [12-ai-engineer-competencies.md](12-ai-engineer-competencies.md) — full competency map

Mobile got you here. **Context, specs, and verification** make you an AI engineer.
