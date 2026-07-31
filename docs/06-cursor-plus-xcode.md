# Cursor + Xcode dual workflow

Cursor does not replace Xcode for iOS. This is the permanent workflow.

## Division of labor

```
┌─────────────────────────────────────────────────────────┐
│  CURSOR                                                 │
│  Spec · Plan Mode · Agent edits · Rules · LEARNINGS     │
└───────────────────────────┬─────────────────────────────┘
                            │ you review diffs
                            ▼
┌─────────────────────────────────────────────────────────┐
│  XCODE                                                  │
│  ⌘B build · ⌘R run · breakpoints · signing · TestFlight│
└─────────────────────────────────────────────────────────┘
```

## Session ritual (15 min overhead, saves hours)

1. Open **both** apps on the same repo folder
2. Xcode: open `StarterApp.xcodeproj`, pick simulator
3. Cursor: open repo root, read today's exercise
4. Work in Cursor until a diff is ready
5. Verify in Xcode before marking exercise done

## Intel Mac / no Xcode MCP

You are **not** missing core features. MCP is optional ([docs](https://cursor.com/docs/integrations/xcode)):

- Requires Xcode 26.3+, macOS 26+, Apple Silicon for full agentic stack
- Intel: use terminal `xcodebuild` if you want CLI builds from Cursor

```bash
cd sample-app/StarterApp
xcodebuild -scheme StarterApp -destination 'platform=iOS Simulator,name=iPhone 16' build
```

## Applying to your own app

Copy into your project:

1. [AGENTS.md](../AGENTS.md) — adapt stack section
2. `.cursor/rules/` — one Swift/SwiftUI rule file
3. [LEARNINGS.md](../LEARNINGS.md) — keep the habit

Keep Xcode as verify. Always.

## Week 1 complete?

Check [07-week-1-syllabus.md](07-week-1-syllabus.md) checklist.

Apply the same loop on a real feature in **your** app next.
