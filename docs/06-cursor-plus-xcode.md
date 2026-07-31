# Optional sandbox: verifying StarterApp edits

**This is not the end goal.** Exercises 01–08 use StarterApp so verify *habits* land on familiar UI. Graduation and real work use **your project's verifiers** — tests, curl, scripts, CI — not "did the simulator look fine."

See [14-verification-practices.md](14-verification-practices.md) · [05-verify-loop.md](05-verify-loop.md).

---

## If you touch SwiftUI in the sandbox

Pick **one** automated path (CLI preferred — no IDE lock-in):

```bash
cd sample-app/StarterApp
xcodebuild -scheme StarterApp -destination 'platform=iOS Simulator,name=iPhone 16' build
```

Optional: open `StarterApp.xcodeproj` and ⌘R for manual UX checks.

Run **in parallel** with human diff review and `/review-bugbot` on `sample-app/`.

---

## Cursor + Xcode (only if you already live in iOS)

Many mobile devs keep both apps open. That is fine for the sandbox — it is **not** the AI engineer graduation bar.

```
Cursor  → spec, context, delegate, review
Xcode   → optional sandbox runtime for StarterApp only
```

Week 3+: verify in whatever proves **your** task (API test, script exit code, PR green, etc.).

---

## Intel Mac / no Xcode MCP

MCP is optional ([docs](https://cursor.com/docs/integrations/xcode)). `xcodebuild` from terminal is enough for sandbox build verify.

---

## Applying to your own project

Copy:

1. [AGENTS.md](../AGENTS.md) — include **verify ritual** (named commands, parallel review)
2. `.cursor/skills/verify-after-edit/` — parallel verify habit
3. [LEARNINGS.md](../LEARNINGS.md)

Define verifiers in AGENTS.md: `npm test`, `pytest`, `curl …`, not "open Xcode."

Next: [07-week-1-syllabus.md](07-week-1-syllabus.md)
