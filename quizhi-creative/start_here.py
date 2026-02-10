#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
秋芝创意 (Quizhi Creative) - Agent Skills Guide
"""

import os
import sys
import json
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_display_width(text):
    import unicodedata
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in ('F', 'W'):
            width += 2
        else:
            width += 1
    return width

def display_header():
    width = 60
    title1 = "秋芝创意 (Quizhi Creative)"
    title2 = "Agent Skills Guide & Builder"
    
    print("╔" + "═" * width + "╗")
    
    pad1 = (width - get_display_width(title1)) // 2
    remain1 = width - get_display_width(title1) - pad1
    print("║" + " " * pad1 + title1 + " " * remain1 + "║")
    
    pad2 = (width - get_display_width(title2)) // 2
    remain2 = width - get_display_width(title2) - pad2
    print("║" + " " * pad2 + title2 + " " * remain2 + "║")
    
    print("╚" + "═" * width + "╝")
    print()

def display_menu():
    print("📋 请选择功能 (Select Function)：")
    print()
    print("1.  🎓 概念指南 (Concept Guide)")
    print("    - 什么是 Agent Skills?")
    print("    - 核心设计原则")
    print()
    print("2.  🛠️ 技能构建器 (Skill Builder)")
    print("    - 创建新技能 (Create New Skill)")
    print("    - 编辑现有技能 (Edit Skill)")
    print()
    print("3.  📤 导出/查看 (Export/View)")
    print("    - 导出为 JSON")
    print("    - 导出为 Markdown")
    print("    - 生成 Mermaid 流程图")
    print()
    print("0.  🚪 退出 (Exit)")
    print()

def concept_guide():
    clear_screen()
    display_header()
    print("🎓 Agent Skills 概念指南")
    print("-" * 60)
    print("""
Agent Skills 是赋予 AI 代理特定能力的模块化组件。
Agent Skills are modular components that empower AI agents with specific capabilities.

核心原则 (Core Principles):
1.  **单一职责 (Single Responsibility)**: 每个 Skill 只做一件事。
2.  **明确输入/输出 (Clear I/O)**: 定义清晰的参数和返回值。
3.  **工具调用 (Tool Use)**: 技能可以调用外部工具 (如 web_search, database)。
4.  **状态无感 (Stateless)**: 理想情况下，技能不依赖外部状态。

示例 (Example):
-   `WeatherSkill`: 获取天气信息。
-   `EmailSkill`: 发送邮件。
-   `DataAnalysisSkill`: 分析 CSV 数据。
""")
    input("\n按回车键返回主菜单...")

def skill_builder():
    clear_screen()
    display_header()
    print("🛠️ 技能构建器 (Skill Builder)")
    print("-" * 60)
    
    name = input("请输入技能名称 (Skill Name): ").strip()
    description = input("请输入技能描述 (Description): ").strip()
    tools = input("所需工具 (Tools, comma separated): ").strip().split(',')
    
    skill = {
        "name": name,
        "description": description,
        "tools": [t.strip() for t in tools],
        "created_at": datetime.now().isoformat()
    }
    
    # Save to file
    filename = f"{name.replace(' ', '_').lower()}_skill.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(skill, f, indent=4, ensure_ascii=False)
        
    print(f"\n✅ 技能已保存至: {filename}")
    input("\n按回车键返回主菜单...")

def export_skills():
    clear_screen()
    display_header()
    print("📤 导出/查看 (Export/View)")
    print("-" * 60)
    
    # List current skills (json files)
    files = [f for f in os.listdir('.') if f.endswith('_skill.json')]
    if not files:
        print("❌ 未找到技能文件。请先使用构建器创建技能。")
        input("\n按回车键返回主菜单...")
        return

    print("现有技能:")
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
        
    choice = input("\n请选择要导出的技能 (序号): ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            filename = files[idx]
            with open(filename, 'r', encoding='utf-8') as f:
                skill = json.load(f)
            
            print(f"\n技能: {skill['name']}")
            print(f"描述: {skill['description']}")
            print(f"工具: {', '.join(skill['tools'])}")
            print("-" * 30)
            print("Markdown 预览:")
            print(f"# {skill['name']}")
            print(f"> {skill['description']}")
            print(f"- Tools: {', '.join(skill['tools'])}")
            
        else:
            print("❌ 无效选择")
    except ValueError:
        print("❌ 无效输入")
        
    input("\n按回车键返回主菜单...")

def main():
    while True:
        clear_screen()
        display_header()
        display_menu()
        choice = input("请输入您的选择 (0-3): ").strip()
        
        if choice == '1':
            concept_guide()
        elif choice == '2':
            skill_builder()
        elif choice == '3':
            export_skills()
        elif choice == '0':
            print("👋 再见！")
            sys.exit(0)
        else:
            input("❌ 无效选择，按回车重试...")

if __name__ == "__main__":
    main()
