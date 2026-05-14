#!/usr/bin/env python3
"""
MiniMax Vision 图片识别工具
用法:
  分析单张图片: python minimax_vision.py analyze <image_path> [prompt]
  对比两张图片: python minimax_vision.py compare <baseline_path> <actual_path>
"""
import sys
import os
import base64
import requests
from PIL import Image, ImageDraw

DEFAULT_PROMPT = "请详细描述这张图片的内容，包括其中的文字、布局、元素等。"
DEFAULT_COMPARE_PROMPT = """请对比这张拼接图片：左边 BASELINE 为期望界面，右边 ACTUAL 为本次截图。

判别规则：
1. 若左右在整体布局、主要控件位置与样式上实质一致，仅时间、数字、列表数据等动态内容不同，视为无问题：has_diff=false。
2. 若存在明确的产品/设计改版（界面有意调整且可接受为新基线）：has_diff=true，is_ui_change=true。
3. 若存在错位、截断、错误状态、空白页、明显渲染异常等非预期问题：has_diff=true，is_ui_change=false。

仅输出 JSON：{"has_diff": bool, "diff_description": "...", "is_ui_change": bool, "suggestion": "..."}"""

def image_to_base64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def call_minimax(image_path, prompt):
    api_key = os.environ.get('MINIMAX_API_KEY', '').strip()
    if not api_key:
        api_key = 'sk-cp-eBYEw7ImOYJDNU5T6fWx18TDdVNlJCtT1eX99cbbibw0zGzjQ8DUstAt7TcBhXLjrOR4hYyeV3FqgoNfUzds6vJN4IhhMTY9w1fRwhJlyFQ3fP02_SYn49Y'

    payload = {
        "prompt": prompt,
        "image_url": f"data:image/png;base64,{image_to_base64(image_path)}"
    }

    response = requests.post(
        "https://api.minimaxi.com/v1/coding_plan/vlm",
        json=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        timeout=60
    )

    return response.json().get('content', '')

def create_comparison(baseline_path, actual_path, output_path):
    img1 = Image.open(baseline_path)
    img2 = Image.open(actual_path)
    h = max(img1.height, img2.height)
    img1 = img1.resize((img1.width, h))
    img2 = img2.resize((img2.width, h))
    combined = Image.new('RGB', (img1.width + img2.width + 20, h), (180, 180, 180))
    combined.paste(img1, (0, 0))
    combined.paste(img2, (img1.width + 20, 0))
    draw = ImageDraw.Draw(combined)
    draw.text((img1.width // 2 - 35, 10), "BASELINE", fill=(0, 0, 0))
    draw.text((img1.width + 20 + img2.width // 2 - 25, 10), "ACTUAL", fill=(0, 0, 0))
    combined.save(output_path)
    return output_path

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法:", file=sys.stderr)
        print("  分析单张图片: python minimax_vision.py analyze <image_path> [prompt]", file=sys.stderr)
        print("  对比两张图片: python minimax_vision.py compare <baseline_path> <actual_path>", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1]

    # Windows 环境下设置输出编码为 UTF-8
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    if cmd == 'analyze':
        image_path = sys.argv[2]
        prompt = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_PROMPT
        result = call_minimax(image_path, prompt)
        print(result)

    elif cmd == 'compare':
        if len(sys.argv) < 4:
            print("对比模式需要提供 baseline 和 actual 两个图片路径", file=sys.stderr)
            sys.exit(1)
        baseline_path = sys.argv[2]
        actual_path = sys.argv[3]
        output_path = '/tmp/comparison.png'
        create_comparison(baseline_path, actual_path, output_path)
        result = call_minimax(output_path, DEFAULT_COMPARE_PROMPT)
        print(result)

    else:
        print(f"未知命令: {cmd}，使用 analyze 或 compare", file=sys.stderr)
        sys.exit(1)