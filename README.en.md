[中文](./README.md) · **English**

# 🧰 YuChen-Skills

#### A small collection of Agent Skills I maintain — open-sourced for reuse

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-4-10B981?style=for-the-badge)](#-skills)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

![Cursor](https://img.shields.io/badge/Cursor-Skill-000000?style=flat-square&logo=cursor&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-Skill-3B82F6?style=flat-square)

Each skill was battle-tested in a real project (including App Store review lessons) before landing here. Layout follows the common [Agent Skills](https://agentskills.io) pattern: `SKILL.md` per folder, optional `schema.json`.

- **Skills** — Structured instructions agents load directly; works with Cursor, Claude Code, Codex, OpenCode, and other Skill-capable tools
- **No separate Prompts folder yet** — copy prompts from each `SKILL.md` if you need a paste-only block

---

## 📋 Index

### Skills

| Name | One-liner | Notes |
|---|---|---|
| 🍎 [**app-store-review-precheck**](#app-store-review-precheck) | Pre-submission checklist against Apple's guidelines; outputs pass / gap / blocking items; optional JSON via `schema.json` | [Post-mortem article](https://github.com/orange-gi/zhiyuxing/blob/main/docs/开发记录博客/六个月开发四次审核知与行上架iOS商店.md) (Chinese, in zhiyuxing repo) |
| ✍️ [**zhiyuxing-writer**](#zhiyuxing-writer) | Zhiyuxing's WeChat public account long-form writing skill with 4-layer self-review | [content_methodology.md](./zhiyuxing-writer/references/content_methodology.md) |
| 👁️ [**minimax-vision**](#minimax-vision) | MiniMax Vision image understanding, supports single image analysis and image comparison | [platform.minimaxi.com](https://platform.minimaxi.com/docs/coding-plan/mcp-guide) |
| 📝 [**dev-report**](#dev-report) | Generate development reports from code changes, record problem background and solutions | [Template source](./develop-report.md) |

---

## 📦 Install

In any agent that supports Skills:

```
Install this skill: https://github.com/orange-gi/yuchen-skills/tree/main/<skill-name>
```

Replace `<skill-name>` with the folder name, e.g. `app-store-review-precheck`.

**Manual**: copy the folder into `.cursor/skills/`, `skills/`, or wherever your team expects skills, then `@` reference it in chat.

---

## ✨ Skills

### app-store-review-precheck

> App Store Pre-check · *It won't click through App Store Connect for you — but it can cut down Guideline surprise mail.*

Before you submit to **App Store Connect**, walk the repo against **iOS code and metadata** (permission strings, auto‑renewable subscriptions, IAP sandbox, account deletion, review credentials, login gating, third‑party AI disclosure & consent). Deliver **pass / gap / blocking** lists; emit a JSON report using **`schema.json`** when you want a paper trail.

**Good for**

- iOS apps with subscriptions / IAP, accounts, sensitive APIs, or third‑party model APIs — pre-review or after a rejection
- When you want the agent to **grep real paths** (plist, purchase UI, privacy copy) and cite evidence

**Not good for**

- Filling in Connect for you, accepting agreements, or legal advice
- A **guarantee of approval** — Apple has the final say; this only reduces predictable misses

**Out of scope**

- No Connect form filling, no "we promise approval"; interpret guidelines via Apple's current [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).

→ [SKILL.md](./app-store-review-precheck/SKILL.md) · [schema.json](./app-store-review-precheck/schema.json) · [Post-mortem (Chinese)](https://github.com/orange-gi/zhiyuxing/blob/main/docs/开发记录博客/六个月开发四次审核知与行上架iOS商店.md)

---

### zhiyuxing-writer

> Long-form writing · *"An informed ordinary person earnestly chatting about something that moves them."*

Zhiyuxing's WeChat public account writing skill, generating articles in that account's style with 4-layer self-review to ensure "human feel."

**Good for**

- Writing WeChat long-form articles, continuing articles, producing long-form content from materials
- When user provides PDF, brief, news link, voice-to-text, etc. saying "write an article for me"

**Not good for**

- Short content (Xiaohongshu posts, Twitter, Moments)
- Pure title/summary generation

**Core features**

- Material understanding and topic judgment (HKR quality check)
- Clear boundary between AI and human roles
- Five article archetype writing methods
- Four-layer self-review system (L1 hard rules → L4 human feel final review)

→ [SKILL.md](./zhiyuxing-writer/SKILL.md) · [content_methodology.md](./zhiyuxing-writer/references/content_methodology.md) · [style_examples.md](./zhiyuxing-writer/references/style_examples.md)

---

### minimax-vision

> Image understanding · *MiniMax Vision image understanding, supports single image analysis and image comparison.*

MiniMax Vision image understanding skill, supports analyzing single image content and comparing differences between two images.

**Good for**

- Analyzing screenshots, identifying interface issues
- Comparing differences between two images
- Understanding content in images

**Commands**

```bash
# Analyze single image
python minimax-vision/minimax_vision.py analyze screenshot.png "describe image content"

# Compare two images
python minimax-vision/minimax_vision.py compare baseline.png actual.png
```

→ [SKILL.md](./minimax-vision/SKILL.md) · [minimax_vision.py](./minimax-vision/minimax_vision.py) · [Official docs](https://platform.minimaxi.com/docs/coding-plan/mcp-guide)

---

### dev-report

> Development report writing · *Generate development reports from code changes, record problem background and solutions.*

Generate structured development reports from code changes, including root cause analysis, solution comparison, and summary.

**Report structure**

```
Record Date: YYYY-MM-DD

## Problem Background

## Problem List

### Problem 1
**Root Cause Analysis** (chain evidence-level positioning, max 3 rounds)
**Solution**: Short-term vs long-term
**Adopted Solution**:
**Additional Test Cases**:

## Summary
```

**Good for**

- Writing development reports after code changes
- Recording problem analysis and solutions

→ [SKILL.md](./dev-report/SKILL.md) · [Template source](./develop-report.md)

---

## 🌟 About

Maintained by [@orange-gi](https://github.com/orange-gi). Skills evolve with product work (e.g. the [Zhiyuxing](https://zhiyuxing.site) stack). ⭐ if useful; Issues welcome.

For Khazix's broader open skills (writing, research, etc.), see [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills).

---

[MIT License](./LICENSE) · Free to use, modify, and redistribute

Made by [@orange-gi](https://github.com/orange-gi)