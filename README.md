# yuchen-skills

公开存放面向 **Cursor Agent Skills**（或其他兼容 `SKILL.md` + 可选 `schema.json` 的编排）的可复用技能包，便于在多个仓库之间拷贝或作为参考。

## 仓库结构

```
app-store-review-precheck/
├── SKILL.md       # 技能说明与预审清单
└── schema.json    # 预审报告 JSON 结构（可选）
```

## 当前技能

| 目录 | 说明 |
|------|------|
| [app-store-review-precheck](./app-store-review-precheck/) | Apple App Store **提审前**对照 Guideline 做代码与配置自检；输出待补项 / 阻塞项；**不**代填 App Store Connect、**不**承诺过审。 |

## 使用方式

1. 将整个技能目录复制到你的项目（例如 `.cursor/skills/`、`skills/` 或与现有 Agent 约定路径一致）。
2. 在对话里 `@技能路径` 或按各工具的 skill 发现规则引用。
3. 条款解释以 [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) 当期版本为准；本仓库内容为实践清单，非法律意见。

## 许可

MIT（见 [LICENSE](./LICENSE)）。
