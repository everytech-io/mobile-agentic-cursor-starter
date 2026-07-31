# Skills — full guide

Official: [Skills](https://cursor.com/docs/skills) · [Customizing agents](https://cursor.com/learn/customizing-agents)

Skills are **portable workflow packages** the agent loads when relevant — or when you invoke them with `/skill-name`.

## This repo's skill

```
.cursor/skills/swiftui-exercises/
  └── SKILL.md    # loads for sample-app/**/*.swift
```

Browse in Cursor: **Customize → Skills**

## SKILL.md anatomy

```markdown
---
name: my-skill
description: What it does AND when to use it (agent reads this to decide relevance)
paths: sample-app/**/*.swift   # optional scope
---

# Title

Step-by-step instructions for the agent.
```

| Field | Required | Purpose |
|-------|----------|---------|
| `name` | Yes | Lowercase, hyphens; matches folder name |
| `description` | Yes | Trigger text for agent |
| `paths` | No | Only surface when editing matching files |
| `disable-model-invocation: true` | No | Only run when you type `/name` |

## Skill directories (Cursor discovers automatically)

| Path | Scope |
|------|-------|
| `.cursor/skills/` | This project |
| `.agents/skills/` | This project (open standard) |
| `~/.cursor/skills/` | All your projects |

Nested monorepo example:

```
apps/ios/.cursor/skills/deploy-testflight/SKILL.md  # only when working under apps/ios/
```

## Built-in skills you'll use in this course

| Skill | Invoke | Use |
|-------|--------|-----|
| `/create-skill` | Manual | Author a new skill from chat |
| `/create-rule` | Manual | Legacy; prefer skills for most cases |
| `/migrate-to-skills` | Manual | Convert old dynamic rules → skills |
| `/review-bugbot` | Manual | Bug-focused review before ship |

## When to create a skill

Create a skill when:

- Same workflow repeats (verify loop, PR checklist, release notes)
- Same mistake happens twice (NavigationView, wrong iOS API)
- You want `/command`-style invocation

Do **not** create a skill for one-off tasks.

## Author with `/create-skill`

```
/create-skill

Name: verify-after-edit
Description: After edits, run parallel verify — automated command, human diff, /review-bugbot.
Include steps: name verifier, parallel lanes, paste output on fail, LEARNINGS.md.
Scope to sample-app/**/*.swift (optional)
```

Review output in `.cursor/skills/verify-after-edit/SKILL.md` before committing.

## Skills in git

Check skills into the repo so learners and teammates share the same agent behavior.

## Exercise

[Exercise 07 — Create your verify skill](../exercises/07-create-skill.md)

Next: [11-debug-and-review.md](11-debug-and-review.md)
