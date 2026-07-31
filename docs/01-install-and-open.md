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

## 3. Optional: confirm StarterApp builds (sandbox)

Exercises 01–08 use StarterApp as optional SwiftUI practice. You do **not** need Xcode as your end goal — only a named verifier if you touch the sandbox:

```bash
cd sample-app/StarterApp
xcodebuild -scheme StarterApp -destination 'platform=iOS Simulator,name=iPhone 16' build
```

Or open `StarterApp.xcodeproj` and ⌘R once to orient. See [06-cursor-plus-xcode.md](06-cursor-plus-xcode.md).

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

Not required for Day 1. Verification habits: [05-verify-loop.md](05-verify-loop.md).

## Checklist

- [ ] Cursor opens this repo as the workspace root (folder name in sidebar)
- [ ] Agent panel opens with ⌘I
- [ ] You know where `docs/`, `exercises/`, and `sample-app/` live
- [ ] (Optional) One sandbox build command works

Next: [Exercise 01 — Explore](../exercises/01-explore.md)
