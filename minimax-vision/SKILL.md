---
name: minimax-vision
description: |
  MiniMax Vision 图片理解skill。当用户需要分析图片内容、识别界面问题、对比截图差异时使用。触发场景：1）"帮我看看这张图有什么问题"；2）"分析一下这个界面"；3）"对比这两张截图有什么区别"。反例：已有明确代码处理的图片生成、不需要理解图像内容的一般性对话。
---

# MiniMax Vision 图片理解

## 环境变量

- `MINIMAX_API_KEY`：可选，未设置时使用内置默认值

## 命令行用法

### 分析单张图片

```bash
python skills/minimax-vision/minimax_vision.py analyze screenshot.png "描述图片内容"
```

### 对比两张图片

```bash
python skills/minimax-vision/minimax_vision.py compare baseline.png actual.png
```

脚本会自动将两张图片拼接后分析，返回 JSON 格式的对比结果。

## 示例

```python
import subprocess

# 分析单张图片
result = subprocess.run([
    'python', 'skills/minimax-vision/minimax_vision.py',
    'analyze', 'screenshot.png', '这张界面有什么问题？'
], capture_output=True, text=True)
print(result.stdout)

# 对比两张图片
result = subprocess.run([
    'python', 'skills/minimax-vision/minimax_vision.py',
    'compare', 'baseline.png', 'actual.png'
], capture_output=True, text=True)
print(result.stdout)
```

## 官方文档

https://platform.minimaxi.com/docs/coding-plan/mcp-guide#2-understand_image