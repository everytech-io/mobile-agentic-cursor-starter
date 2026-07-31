# Install and open

## 1. Install Cursor

Download from [cursor.com/downloads](https://cursor.com/downloads). Sign in.

Official guide: [Quickstart](https://cursor.com/docs/get-started/quickstart)

## 2. Clone this repo

```bash
git clone https://github.com/everytech-io/mobile-agentic-cursor-starter.git
cd mobile-agentic-cursor-starter
cursor .
```

## 3. Open the sample app in Xcode

```bash
open sample-app/StarterApp/StarterApp.xcodeproj
```

Select an iPhone simulator → **⌘R**. Confirm **HabitPeek** launches.

Keep Xcode open in the background for the rest of the course.

## 4. Learn the Agent shortcut

| Action | Mac shortcut |
|--------|----------------|
| Open Agent | **⌘I** |
| Reference a file | Type `@` + filename in chat |
| Plan Mode | **Shift+Tab** in Agent input |
| Command palette | **⌘⇧P** |

Official: [Your first project](https://cursor.com/help/getting-started/first-project.md)

## 5. Optional: SwiftLint

```bash
brew install swiftlint
cd sample-app/StarterApp && swiftlint
```

Not required for Day 1. We add verify checks in [05-verify-loop.md](05-verify-loop.md).

## Checklist

- [ ] Cursor opens this repo as the workspace root (folder name in sidebar)
- [ ] Agent panel opens with ⌘I
- [ ] HabitPeek runs in simulator
- [ ] You know where `docs/`, `exercises/`, and `sample-app/` live

Next: [Exercise 01 — Explore](../exercises/01-explore.md)
