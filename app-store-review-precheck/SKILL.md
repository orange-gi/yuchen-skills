---
name: app-store-review-precheck
description: |
  对照 Apple App Review 常见条款扫 iOS 代码与配置，列出通过项、待补项与阻塞项；可按 schema.json 输出结构化预审报告。
  不做：代填 Connect、代操作后台与协议、法律结论、承诺过审。
  触发：提审、预审、被拒复盘、Guideline、IAP、订阅、隐私文案、审核账号。
alwaysApply: false
---

# App Store 上架预审（苹果审核前自检）

本 skill 把「真机审核容易卡住的地方」整理成可执行清单，证据来源包括 **Apple 官方 App Review Guidelines** 与本仓库实际上架复盘（`docs/开发记录博客/六个月开发四次审核知与行上架iOS商店.md`）。**不能替代**你在 App Store Connect 里亲手填写与沙盒真机完整点一遍，但能压低第一轮就收到多条 5.x / 3.x 的概率。

**结构化输出**：预审结论可按 `schema.json` 产出 JSON，便于存档或与脚本对齐。

---

## 何时启用

- 准备首次提交或重新提交 iOS / iPadOS 应用
- 应用使用 **相机、相册、麦克风、语音识别、通讯录** 等受保护能力
- 应用含 **自动续订订阅** 或任意 **In-App Purchase**
- 应用含 **账号注册**，且含 **AI、云端推理、第三方模型 API**
- 用户明确要做「过审预审」「对照 Guideline 扫一遍」

---

## Agent 必须交付的预审结果

1. **应用类型摘要**（一句话，是否订阅、是否第三方 AI、是否强制登录）
2. **按下文章节逐条**标注「通过 / 待补 / 不适用」，并给出**证据**（仓库路径、`Info.plist` 键名、组件文件名、或 App Review 备注该怎么写）
3. **阻塞项**单独列表（必须先修再提交）
4. 若仓库信息不够，只列**最少**追问项（禁止泛泛问「有没有合规」）

可选：按 `skills/app-store-review-precheck/schema.json` 输出一份 `precheck_report` JSON。

---

## 1. Purpose Strings（Guideline 5.1.1(ii) 等）

对每个 `UsageDescription` 类文案检查。

- [ ] 说明**用途**，并给出**具体示例**（忌「应用需要访问相册」式空话）。
- [ ] 文案与真实调用的 API 一致；未使用的权限不要声明。

**在本仓库的典型位置**：`zhiyuxing-app/app.json` → `ios.infoPlist` / 插件注入的 `NSMicrophoneUsageDescription`、`NSSpeechRecognitionUsageDescription` 等。

**Agent 动作**：全文搜索 `UsageDescription`、`PhotoLibrary`、`Camera`、`Microphone`、`SpeechRecognition`，对照实际调用。

---

## 2. 自动续订订阅（Guideline 3.1.2(c)）

若存在 auto-renewable subscription，**应用内**购买流程须让用户在同一语境下看到：

- [ ] 订阅名称、时长、价格（及适当情形下单位价）
- [ ] **可点击**且 **HTTPS 可访问** 的隐私政策
- [ ] **可点击**且 **HTTPS 可访问** 的用户协议 / EULA
- [ ] 用户付钱后**具体得到什么**（权益展开写，忌只有「会员」二字）

**App Store Connect 元数据**：

- [ ] Privacy Policy 字段为有效链接
- [ ] EULA 按你使用标准条款或自定义条款的要求放在描述或 Connect 对应栏位

**Agent 动作**：定位付费墙 / `SubscriptionStoreView` / `react-native-iap` 购买 UI，逐链接用逻辑校验（非死链）。

---

## 3. IAP 可用性与商务（Guideline 2.1(b)）

- [ ] **Sandbox** 下购买与恢复购买全流程无报错。
- [ ] 审核侧若出现「产品未就绪」类提示，按商品配置、环境、Paid Apps Agreement 排查（本仓库曾遇此类驳回）。
- [ ] Account Holder 侧 **Paid Apps Agreement** 已生效。

**Agent 动作**：核对 IAP 产品 ID、商品状态；代码路径上对未加载商品须有**可见错误**，禁止静默失败。

---

## 4. 账号删除（Guideline 5.1.1(v)）

若支持**创建账号**：

- [ ] 应用内可**发起删除**（仅停用账号不够）。
- [ ] 若删除在网页完成，提供**直达删除流程**的 URL，而非仅首页。

**本仓库锚点**：`cloudbase/functions/delete-account/` 等与账号注销相关的云函数及 App 内入口文案。

---

## 5. App Review 信息与演示账号（Guideline 2.1 Information Needed）

在 App Store Connect → App Review Information：

- [ ] 审核账号密码正确，复杂流程附**步骤说明**。
- [ ] 若需审「订阅过期后」行为，准备 **订阅已过期的沙盒/演示账号**（苹果曾要求此类账号以走完购买链路）。
- [ ] 备注中说明 AI 入口、付费墙、首次 AI 同意等非显而易见路径。

---

## 6. 登录门槛与「非账号功能」（Guideline 5.1.1(v)）

审核可能认为部分能力应在**未登录**下也可访问。

- [ ] 列出功能 × 是否必须登录；区分「依赖云端用户数据的 AI」与可本地化演示的空状态。
- [ ] 若 IAP 被认定为与非账号内容绑定，检查是否**强迫先注册再购买**（易触发额外条文）。
- [ ] 准备一段**产品设计说明**：为何核心功能必须账号（便于在审核对话里陈述）。

---

## 7. 第三方 AI 与数据传输（Guideline 5.1.1(i)、5.1.2(i)）

若请求发往**第三方模型 API**（如云端大模型）：

- [ ] **首次发送前**告知发送的数据类别、接收方（公司或产品名）。
- [ ] **明示同意**，不同意则不发送。
- [ ] 隐私政策写明收集、用途、第三方共享；**不得**仅用外链代替应用内披露时机。

**Agent 动作**：从 AI 请求封装点到首次调用 UI，沿链路 grep；对照 `zhiyuxing-landing/public/privacy.html` 等与 App 内文案一致。

---

## 8. 官网与 App 一致（建议）

若有对外站点（如 `https://zhiyuxing.site`）：

- [ ] 权益、价格口径与 App 内一致。
- [ ] 隐私政策、用户协议、第三方清单在移动浏览器可打开。

---

## 9. 权威来源

条文解释与范例以 **Apple Developer 当前 App Review Guidelines 与订阅文档** 为准；本 skill 为实践摘要，答复审核时可引用具体 Guideline 编号。

---

## 边界

- 不代替用户在 Connect 内点击协议、创建 IAP、填写元数据。
- 不提供法律意见；涉合规边界提示咨询法务。
- CloudBase / 云函数实现可交叉阅读 `/.agents/skills/cloudbase-guidelines/SKILL.md`。
