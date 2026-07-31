# Expanded plan — 2026-08-01 (rev 2)

> **Status:** Mobile → **AI Engineer** curriculum (Week 1–3)  
> **Repo:** [everytech-io/mobile-agentic-cursor-starter](https://github.com/everytech-io/mobile-agentic-cursor-starter)

## Mission

Transition rusty mobile developers into **AI engineers** — not "Cursor for iOS."

| Week | Role | Where |
|------|------|-------|
| 1–2 | Learn loop + context on **StarterApp sandbox** | SwiftUI + Xcode verify |
| 3 | **Graduate** — same loop on real non-mobile work | Their repo / API / script / ticket |

Core loop:

```
SPEC → CONTEXT → [PLAN] → DELEGATE → VERIFY → REVIEW → CAPTURE
```

---

## Delivered artifacts

| Artifact | Path | Status |
|----------|------|--------|
| AI engineer mindset | `docs/00-ai-engineer-mindset.md` | ✅ |
| Competency matrix | `docs/12-ai-engineer-competencies.md` | ✅ |
| Context engineering | `docs/13-context-engineering.md` | ✅ |
| Week 1–2 mechanics | `docs/00`–`11` | ✅ |
| Exercises 01–09 | `exercises/` (09 = non-mobile graduation) | ✅ |
| StarterApp sandbox | `sample-app/StarterApp/` | ✅ |
| Example context | `AGENTS.md`, `.cursor/skills/` | ✅ |

---

## Week 1 — Level 1: Agent operator

Sandbox only. Competencies: **C1 spec, C4 verify, C9 domain catch**.

| Milestone | Acceptance |
|-----------|------------|
| Mindset + watch-first | Can explain mobile vs AI engineer table |
| Ex 01–02 | SPEC + Xcode verify + LEARNINGS |
| Ex 03 | Plan Mode multi-file |
| Ex 04, 06 | AGENTS.md extended |

---

## Week 2 — Level 2: Context engineer

Competencies: **C2 context, C3 modes, C5 review, C6 memory, C7 plan, C8 debug**.

| Milestone | Acceptance |
|-----------|------------|
| Ex 07 | Custom or ios-verify skill |
| Ex 05 | Debug workflow |
| Ex 08 | Ask → Plan → Agent → review |
| Bugbot | Run once on sample-app diff |

---

## Week 3 — Level 3: AI engineer (mandatory for graduation)

Competency: **C10 transfer**.

| Milestone | Acceptance |
|-----------|------------|
| AGENTS.md copied to learner project | Not tutorial repo only |
| Ex 09 complete | **Non-mobile** task with verifier evidence |
| Verifier | Tests / curl / script / PR — not only Xcode |
| Can teach context stack | 5-min explanation without notes |

Options for Ex 09: script, API, docs, ticket, MCP read-only query.

---

## What "AI engineer" means here (teaching script)

1. **Spec is the product** — done-when is your eval
2. **Context is the job** — AGENTS.md + skills + plans in git
3. **Delegate, don't type** — agent + subagents + MCP
4. **Verify with evidence** — mobile devs already know this; generalize it
5. **Domain beats model** — you own truth tables, APIs, deployment targets
6. **Close the loop** — review → merge → LEARNINGS → skill

StarterApp is **gym**. Week 3 is **the job**.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Stops at SwiftUI | Week 3 + Ex 09 required for "graduate" |
| Thinks prompting = AI engineering | Mindset doc + context engineering doc |
| No verifier on real work | Ex 09 rubric requires command output / PR |
| Copilot habits | SPEC + REVIEW gates every exercise |

---

## Phase 4 — EveryTech packaging

- [ ] Facilitator guide: Week 3 is not optional
- [ ] Link from everytech-products
- [ ] Pilot: measure **Ex 09 completion**, not Ex 02
- [ ] Optional: MCP week, Cloud Agents, Every* adapter module

---

## Metrics (pilot)

| Metric | Target |
|--------|--------|
| Level 1 (Week 1) | ≥ 70% complete Ex 1–4 |
| Level 2 (Week 2) | ≥ 50% complete Ex 5–8 |
| **Level 3 (Week 3)** | ≥ 40% complete **Ex 09** |
| Ex 09 with non-Xcode verifier | 100% of Level 3 |

---

## Revision log

| Date | Change |
|------|--------|
| 2026-08-01 | Rev 2 — reframe mobile sandbox → AI engineer; Week 3 + Ex 09 |
| 2026-08-01 | Rev 1 — skills, Plan, Debug, Bugbot |
