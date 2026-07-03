**中文** · [English](./README.en.md)

# 🧰 YuChen-Skills

#### 个人维护的 Agent Skills 合集，顺手开源

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-4-10B981?style=for-the-badge)](#-skills)
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
| ✍️ [**zhiyuxing-writer**](#zhiyuxing-writer) | 知与行公众号长文写作 skill，按该账号风格生成文章并进行四层自检 | [content_methodology.md](./zhiyuxing-writer/references/content_methodology.md) |
| 👁️ [**minimax-vision**](#minimax-vision) | MiniMax Vision 图片理解，支持单图分析和双图对比 | [platform.minimaxi.com](https://platform.minimaxi.com/docs/coding-plan/mcp-guide) |
| 📝 [**dev-report**](#dev-report) | 根据代码修改生成开发报告，记录问题背景、解决方案和总结 | [模板来源](./develop-report.md) |
| 🔎 [**xquik-social-research**](#xquik-social-research) | 用 Xquik 的 X 数据分析受众主题、创作者分层、发布信号与竞品动态 | [docs.xquik.com](https://docs.xquik.com/api-reference/introduction) |

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

### zhiyuxing-writer

> 公众号长文写作 · *「有见识的普通人在认真聊一件打动他的事。」*

知与行公众号长文写作 skill，按照该账号的风格生成文章，并进行四层自检确保"活人感"。

**适合**

- 撰写公众号长文、续写文章、根据素材产出长文
- 用户丢过来 PDF、brief、新闻链接、语音转文字等素材说"帮我写篇文章"

**不适合**

- 短内容（小红书帖子、推特、朋友圈）
- 纯标题摘要生成

**核心功能**

- 理解素材与选题判断（HKR 质检）
- 明确 AI 与人的角色边界
- 五种文章原型写作方法
- 四层自检体系（L1 硬性规则 → L4 活人感终审）

→ [SKILL.md](./zhiyuxing-writer/SKILL.md) · [content_methodology.md](./zhiyuxing-writer/references/content_methodology.md) · [style_examples.md](./zhiyuxing-writer/references/style_examples.md)

---

### minimax-vision

> 图片理解 · *「MiniMax Vision 图片理解，支持单图分析和双图对比。」*

MiniMax Vision 图片理解 skill，支持分析单张图片内容和对比两张图片差异。

**适合**

- 分析截图、识别界面问题
- 对比两张图片的差异
- 理解图片中的内容

**命令**

```bash
# 分析单张图片
python minimax-vision/minimax_vision.py analyze screenshot.png "描述图片内容"

# 对比两张图片
python minimax-vision/minimax_vision.py compare baseline.png actual.png
```

→ [SKILL.md](./minimax-vision/SKILL.md) · [minimax_vision.py](./minimax-vision/minimax_vision.py) · [官方文档](https://platform.minimaxi.com/docs/coding-plan/mcp-guide)

---

### dev-report

> 开发报告编写 · *「根据代码修改生成开发报告，记录问题背景、解决方案和总结。」*

根据代码修改内容生成结构化开发报告，包含根因分析、方案对比和总结。

**报告结构**

```
记录日期：YYYY-MM-DD

## 问题背景

## 问题列表

### 问题一
**根因分析**（链式证据级定位，最多3轮）
**方案**：短期方案 vs 长远方案
**采纳方案**：
**补充用例**：

## 小结
```

**适合**

- 代码修改完成后编写开发报告
- 记录问题分析和解决方案

→ [SKILL.md](./dev-report/SKILL.md) · [模板来源](./develop-report.md)

---

### xquik-social-research

> X 社交研究 · *把 Xquik 数据整理成有证据的受众和市场信号。*

分析 Xquik 导出的 JSON / CSV、REST API 响应或 MCP 输出，总结 X 对话主题、创作者分层、发布信号与竞品动态。

**适合**

- 基于 X 帖子、账号、搜索、趋势或粉丝数据做受众研究
- 发布前调研、竞品监控、创作者发现
- 把 Xquik 数据整理成内容和活动建议

**不适合**

- 垃圾信息、凭证收集或绕过访问控制
- 脱离用户提供或 Xquik 返回数据的泛化判断

→ [SKILL.md](./xquik-social-research/SKILL.md) · [Xquik API 文档](https://docs.xquik.com/api-reference/introduction) · [MCP 文档](https://docs.xquik.com/mcp/overview)

---

## 🌟 关于

本仓库由 [@orange-gi](https://github.com/orange-gi) 维护，与「知与行」等产品迭代中沉淀的预审清单同步演进。若有用欢迎 ⭐；问题或改进欢迎 Issues。

若你也关注卡兹克开源的通用写作 / 调研类 skill，可见 [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)。

---

[MIT License](./LICENSE) · 自由使用 / 修改 / 再分发

Made by [@orange-gi](https://github.com/orange-gi)
