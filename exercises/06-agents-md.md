# Exercise 06 — AGENTS.md for your workflow

**Goal:** Extend project AGENTS.md so Agent knows *your* verify ritual.  
**Time:** ~30 min  
**Read first:** [docs/09-agents-md.md](../docs/09-agents-md.md), [docs/14-verification-practices.md](../docs/14-verification-practices.md)

## Task

Add a **## Verify ritual** section to [AGENTS.md](../AGENTS.md) with your personal checklist:

```markdown
## Verify ritual (learner: customize)

After any agent edit (parallel — start all lanes when diff is ready):
1. Automated: <name command — xcodebuild, npm test, pytest, curl, …>
2. Human: read diff + walk done-when path
3. Agent review: /review-bugbot on changed paths
4. Append LEARNINGS.md if anything surprised me
```

For StarterApp sandbox only, example automated command:

```bash
xcodebuild -scheme StarterApp -destination 'platform=iOS Simulator,name=iPhone 16' build
```

## Prompt (optional)

```
@AGENTS.md

Add a "Verify ritual" section per docs/09-agents-md.md and docs/14-verification-practices.md.
Encode parallel lanes. Keep file under 80 lines. Do not remove intentional exercise gaps.
```

## Done when

- [ ] AGENTS.md has Verify ritual with **named commands** (not "open Xcode")
- [ ] Mentions parallel human + agent review
- [ ] LEARNINGS entry: one line on what AGENTS.md saved you from repeating

Next: [07-create-skill.md](07-create-skill.md)
