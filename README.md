**中文** · [English](./README.en.md)

# 🧰 YuChen-Skills

#### 个人维护的 Agent Skills 合集，顺手开源

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-1-10B981?style=for-the-badge)](#-skills)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

![Cursor](https://img.shields.io/badge/Cursor-Skill-000000?style=flat-square&logo=cursor&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-Skill-3B82F6?style=flat-square)

技能在项目里跑通过一轮（含真实上架踩坑总结），才放进仓库。结构遵循 [Agent Skills](https://agentskills.io) 常见约定（目录内 `SKILL.md`，可选 `schema.json`）。

- **Skills** — Agent 直接加载的结构化指令；可与 Cursor、Claude Code、Codex、OpenCode 等兼容 Skill 的发现方式配合使用
- **本仓库暂无独立 Prompts 合集** — 需要可复制提示词可自行从各 Skill 正文截取

---

## 📋 目录

### Skills

| 名字 | 一句话 | 讲解 |
|---|---|---|
| 🍎 [**app-store-review-precheck**](#app-store-review-precheck) | 提审前对照 Apple Guideline 扫代码与配置，列出通过 / 待补 / 阻塞；可按 `schema.json` 输出结构化报告 | [上架复盘长文](https://github.com/orange-gi/zhiyuxing/blob/main/docs/开发记录博客/六个月开发四次审核知与行上架iOS商店.md)（知与行仓库） |

---

## 📦 安装方式

在支持 Skill 的 Agent（Cursor、Claude Code、Codex、OpenClaw 等）里，可以直接说：

```
帮我安装这个 skill：https://github.com/orange-gi/yuchen-skills/tree/main/<skill-name>
```

把 `<skill-name>` 换成目录名，例如 `app-store-review-precheck`。由 Agent 把对应子目录放到你项目约定的 skills 路径即可。

**手动安装**：将 `app-store-review-precheck/` 整夹复制到例如 `.cursor/skills/`、`skills/` 或与团队约定目录，再在对话里 `@` 引用。

---

## ✨ Skills

### app-store-review-precheck

> App Store 预审 · *「不能代你点完 Connect，但能帮你少收几封 Guideline 邮件。」*

在提交 **App Store Connect** 之前，按清单对照 **iOS 工程与元数据**（权限文案、自动续订订阅、IAP 沙盒、账号删除、审核演示账号、登录门槛、第三方 AI 披露与同意等），输出 **通过项 / 待补项 / 阻塞项**；需要存档时可按 **`schema.json`** 生成 JSON 报告。

**适合**

- 含订阅 / IAP、账号、相册麦克风等权限、或第三方模型 API 的 iOS 应用准备提审或被拒复盘
- 想让 Agent 在仓库里 **grep 配置与代码路径**，给出可核对的证据链

**不适合**

- 指望 skill **替你填写** App Store Connect、**代替勾选协议**、或给出 **法律结论**
- 需要 **保证过审** — 清单只能降概率，最终以 Apple 审核为准

**它不做什么（边界）**

- 不代填 Connect、不代替后台操作、不承诺过审；条款解释以 [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) 当期版本为准。

→ [SKILL.md](./app-store-review-precheck/SKILL.md) · [schema.json](./app-store-review-precheck/schema.json) · [上架复盘长文](https://github.com/orange-gi/zhiyuxing/blob/main/docs/开发记录博客/六个月开发四次审核知与行上架iOS商店.md)

---

## 🌟 关于

本仓库由 [@orange-gi](https://github.com/orange-gi) 维护，与「知与行」等产品迭代中沉淀的预审清单同步演进。若有用欢迎 ⭐；问题或改进欢迎 Issues。

若你也关注卡兹克开源的通用写作 / 调研类 skill，可见 [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)。

---

[MIT License](./LICENSE) · 自由使用 / 修改 / 再分发

Made by [@orange-gi](https://github.com/orange-gi)
