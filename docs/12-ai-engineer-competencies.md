# AI engineer competencies

Map of what you are building — use as self-assessment and mentor rubric.

Official backdrop: [What is agentic coding?](https://cursor.com/help/ai-features/agentic-coding) · [Customizing agents](https://cursor.com/learn/customizing-agents)

---

## Competency matrix

| # | Competency | Mobile-only? | How you prove it in this course |
|---|------------|--------------|----------------------------------|
| C1 | **Spec writing** | No | Every exercise starts with goal / done-when / out-of-scope |
| C2 | **Context engineering** | No | AGENTS.md, skills, `@` mentions ([09](09-agents-md.md), [10](10-skills.md), [13](13-context-engineering.md)) |
| C3 | **Mode routing** | No | Ask vs Plan vs Agent vs Debug ([08](08-cursor-modes.md)) |
| C4 | **Verification discipline** | No | Parallel lanes: automated + human + agent review ([05](05-verify-loop.md), [14](14-verification-practices.md)) |
| C5 | **Review gates** | No | `/review-bugbot` before "done" ([11](11-debug-and-review.md)) |
| C6 | **Durable memory** | No | LEARNINGS.md → skill when repeat ([04](04-rules-and-context.md)) |
| C7 | **Plan before multi-step work** | No | Plan Mode + saved plans ([03](03-plan-mode.md)) |
| C8 | **Debug with evidence** | No | Debug Mode / logs, not guesses ([11](11-debug-and-review.md)) |
| C9 | **Domain authority** | No | You catch wrong APIs; agent doesn't ([00-ai-engineer-mindset](00-ai-engineer-mindset.md)) |
| C10 | **Transfer to non-mobile work** | **Graduation** | [Exercise 09](../exercises/09-ai-engineer-graduation.md) |

| C4 on sandbox | ShipGate pytest/curl — graduation uses **your** verifiers |

---

## Level rubric

### Level 0 — Copilot user
Uses AI for snippets. No spec. No verify ritual. Same mistakes every session.

### Level 1 — Agent operator (Week 1 graduate)
Runs Agent with mini-spec. Parallel verify (automated + human + review). Writes LEARNINGS.

### Level 2 — Context engineer (Week 2 graduate)
Maintains AGENTS.md + skills. Uses Plan and Debug modes. Runs review before done.

### Level 3 — AI engineer (Week 3 graduate)
Same loop on **non-mobile** work: API change, script, doc pipeline, Jira ticket, MCP tool.
Owns spec → plan → delegate → verify → ship. Domain knowledge leads; agent accelerates.

---

## Week 3 topics (AI engineer, not mobile)

| Topic | Why it matters |
|-------|----------------|
| MCP (GitHub, docs, DB) | Agents need **tools**, not just files |
| Subagents / Cloud Agents | Delegate exploration; you keep verify |
| CLI agent (`agent` command) | Same loop in CI and terminal |
| Skill as product | Encode team workflow in git |
| Eval mindset | Done-when = eval; LEARNINGS = regression log |
| Full ship loop | Spec → PR → review → merge (not stop at diff) |

Docs: [official-cursor-links.md](official-cursor-links.md) · Phase 4 in [HIGH-LEVEL-PLAN.md](HIGH-LEVEL-PLAN.md)

---

## Anti-patterns (instant fail for "AI engineer")

| Anti-pattern | Fix |
|--------------|-----|
| "The agent said it's done" | Show verifier output |
| Re-prompting instead of reverting plan | Revert → refine plan → rebuild |
| 500-line AGENTS.md | Split into skills |
| No LEARNINGS after failure | Capture or repeat forever |
| Mobile skills only | Week 3 on your real stack; ShipGate L4 or own repo |

---

## Graduation

Complete [Exercise 09](../exercises/09-ai-engineer-graduation.md) — one **non-mobile** agent task with full loop.

Next: [13-context-engineering.md](13-context-engineering.md)
