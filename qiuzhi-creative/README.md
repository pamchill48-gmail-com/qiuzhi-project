# 秋芝创意引擎 (Qiuzhi Creative Engine)
# Qiuzhi Creative Engine

秋芝餐厅的核心创意生成模块。基于 Google Gemini 模型，提供智能文案与视觉设计支持。
The core creative generation module for Qiuzhi Restaurant. Powered by Google Gemini, providing intelligent copywriting and visual design support.

---

## 🛠️ 功能特性
## 🛠️ Features

-   **智能文案生成**：自动生成符合品牌调性的营销文案。
    **Smart Copywriting**: Automatically generates marketing copy that aligns with the brand tone.
-   **视觉设计辅助**：生成菜单、海报的布局建议与配色方案。
    **Visual Design Aid**: Generates layout suggestions and color schemes for menus and posters.
-   **图像生成集成**：通过 `generate_image.py` 脚本调用 Gemini 绘图能力。
    **Image Generation Integration**: Invokes Gemini's drawing capabilities via the `generate_image.py` script.

---

## 📂 模块结构
## 📂 Module Structure

-   `scripts/`: 包含图像生成等核心 Python 脚本。
    Contains core Python scripts like image generation.
-   `assets/`: 存放生成过程中需要的静态资源（如 Logo 模板）。
    Stores static assets needed during generation (e.g., Logo templates).
-   `SKILL.md`: 技能定义文件，用于集成到 OpenClaw 等 Agent 系统。
    Skill definition file for integration into Agent systems like OpenClaw.

---

## 🚀 使用方法
## 🚀 Usage

该模块主要通过根目录的 `start_here.py` 调用，也可以单独使用脚本：
This module is primarily invoked via `start_here.py` in the root directory, or scripts can be used independently:

```bash
# 单独生成图像
uv run scripts/generate_image.py --prompt "美味的汉堡" --filename "burger.png"
```
