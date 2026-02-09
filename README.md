# 求知项目 (Clawdbot Skill Demo)
# Qiuzhi Project (Clawdbot Skill Demo)

一个简单、易于 Fork 且支持 Codespace 的 Python 项目，用于演示 **Google Gemini API** 的集成。
A simple, fork-able, and Codespace-ready Python project to demonstrate **Google Gemini API** integration.

---

## 🚀 快速开始 (30 秒)
## 🚀 Quick Start (30 Seconds)

如果您使用 GitHub Codespaces，则无需安装任何环境！
No installation required if you use GitHub Codespaces!

1.  **Fork 此仓库**
    **Fork this Repository**
    点击页面右上角的 **Fork** 按钮。
    Click the **Fork** button at the top right of this page.

2.  **在 Codespaces 中打开**
    **Open in Codespaces**
    - 点击绿色的 **Code** 按钮。
      Click the green **Code** button.
    - 切换到 **Codespaces** 标签页。
      Switch to the **Codespaces** tab.
    - 点击 **Create codespace on main**。
      Click **Create codespace on main**.

3.  **运行演示**
    **Run the Demo**
    终端准备好后，运行以下命令：
    Once the terminal is ready, run:

    ```bash
    # 安装依赖 / Install dependencies
    pip install google-generativeai

    # 运行演示 (需要 API Key) / Run the demo (Requires GOOGLE_API_KEY)
    export GOOGLE_API_KEY="your_api_key_here"
    python3 start_here.py
    ```

---

## 🔑 必要条件
## 🔑 Requirements

运行此项目需要：
To run this project, you need:

-   **Google Gemini API Key**: 可在 [Google AI Studio](https://aistudio.google.com/) 免费获取。
    **Google Gemini API Key**: Get one for free at [Google AI Studio](https://aistudio.google.com/).

---

## 📂 项目结构
## 📂 Project Structure

-   `start_here.py`: 入口脚本。从这里开始！
    The entry point script. Start here!
-   `demo_system.py`: 演示系统交互。
    Demonstrates system interactions.
-   `test_image_gen.py`: 测试图像生成能力（如果可用）。
    Tests image generation capabilities (if available).
-   `test_skill.py`: 验证技能集成。
    Validates skill integration.

---

## 🤝 贡献
## 🤝 Contributing

欢迎 Fork 并提交 Pull Request！本项目旨在作为您 AI 实验的一个简单起点。
Feel free to fork and submit Pull Requests! This project is designed to be a simple starting point for your own AI experiments.
