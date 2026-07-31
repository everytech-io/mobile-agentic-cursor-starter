# Week 1 syllabus

Structured path for a rusty mobile developer learning Cursor + agentic workflow.

## Outcomes (end of week)

You can:

- Open a repo, orient with Agent, and scope a one-screen change
- Write a mini-spec (goal / done-when / out-of-scope)
- Use Plan Mode for multi-file features
- Review diffs and verify in Xcode before trusting Agent output
- Maintain `LEARNINGS.md` and one `.cursor/rules` file

## Schedule

| Day | Read | Exercise | Time | Deliverable |
|-----|------|----------|------|-------------|
| 1 | [00-start-here](00-start-here.md), [01-install](01-install-and-open.md), [02-day-1](02-day-1-explore-and-edit.md) | [01-explore](../exercises/01-explore.md), [02-small-change](../exercises/02-small-change.md) | ~90 min | Empty state works in simulator |
| 2 | [05-verify-loop](05-verify-loop.md) | Finish 02 if needed; re-run verify checklist | ~45 min | LEARNINGS entry #1 |
| 3 | [03-plan-mode](03-plan-mode.md) | [03-plan-feature](../exercises/03-plan-feature.md) | ~90 min | Habit detail screen + navigation |
| 4 | [04-rules-and-context](04-rules-and-context.md) | [04-capture-learning](../exercises/04-capture-learning.md) | ~60 min | One new rule + LEARNINGS #2–3 |
| 5 | [06-cursor-plus-xcode](06-cursor-plus-xcode.md) | Re-ship 03 cold in Xcode only verify | ~45 min | Full dual-app loop without notes |
| 6–7 | [official-cursor-links](official-cursor-links.md) | Apply loop to **your** app | optional | AGENTS.md in your repo |

## Completion checklist

- [ ] Completed exercises 01–04
- [ ] At least 3 entries in LEARNINGS.md
- [ ] Built and ran HabitPeek after every Agent session
- [ ] Used Plan Mode at least once
- [ ] Used `@` to reference specific files at least twice
- [ ] Read [Agent overview](https://cursor.com/docs/agent/overview) and [agentic coding](https://cursor.com/help/ai-features/agentic-coding.md)

## What comes after Week 1

| Topic | Resource |
|-------|----------|
| Skills (repeatable workflows) | [cursor.com/docs/skills](https://cursor.com/docs/skills) |
| MCP (GitHub, Jira, etc.) | [cursor.com/docs/mcp](https://cursor.com/docs/mcp) |
| Every* adapter pattern | Your team's mobile integration standards |
| Xcode MCP (M-series only) | [cursor.com/docs/integrations/xcode](https://cursor.com/docs/integrations/xcode) |

## Teaching note (for mentors)

Do not start with MCP, subagents, or telco ontologies. Start with **verify in Xcode**. The failure mode for rusty mobile devs is faster hallucinations, not faster shipping.
