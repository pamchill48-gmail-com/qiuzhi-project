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
    print()
    print("3.  📤 导出/查看 (Export/View)")
    print("    - 导出为 JSON/Markdown")
    print()
    print("4.  🚀 进阶功能 (Advanced Features) ✨")
    print("    - 自动生成脚手架 (Scaffold)")
    print("    - 逻辑模拟器 (Simulator)")
    print("    - Mermaid 流程图生成")
    print()
    print("0.  🚪 退出 (Exit)")
    print()

def advanced_menu():
    while True:
        clear_screen()
        display_header()
        print("🚀 进阶功能 (Advanced Features)")
        print("-" * 60)
        
        # List current skills
        files = [f for f in os.listdir('.') if f.endswith('_skill.json')]
        if not files:
            print("❌ 未找到技能文件。请先使用构建器创建技能。")
            input("\n按回车键返回...")
            return

        print("请选择一个技能进行进阶操作:")
        for i, f in enumerate(files):
            print(f"{i+1}. {f}")
        
        choice = input("\n请选择技能序号 (或 0 返回): ").strip()
        if choice == '0': break
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                filename = files[idx]
                with open(filename, 'r', encoding='utf-8') as f:
                    skill_data = json.load(f)
                
                process_advanced_choice(skill_data)
            else:
                print("❌ 无效选择")
        except ValueError:
            print("❌ 无效输入")

def process_advanced_choice(skill_data):
    while True:
        clear_screen()
        display_header()
        print(f"当前操作技能: {skill_data['name']}")
        print("-" * 60)
        print("1. 🏗️  生成脚手架 (Generate Scaffold)")
        print("2. 🧪 逻辑模拟器 (Run Simulator)")
        print("3. 📊 生成 Mermaid 流程图 (Mermaid Flow)")
        print("0. 返回上一级")
        
        sub_choice = input("\n请输入选择 (0-3): ").strip()
        if sub_choice == '0': break
        
        if sub_choice == '1':
            generate_scaffold(skill_data)
        elif sub_choice == '2':
            run_simulator(skill_data)
        elif sub_choice == '3':
            generate_mermaid(skill_data)

def generate_scaffold(skill_data):
    skill_dir = f"skills/{skill_data['name'].replace(' ', '_').lower()}"
    os.makedirs(f"{skill_dir}/scripts", exist_ok=True)
    
    # Create SKILL.md
    with open(f"{skill_dir}/SKILL.md", 'w', encoding='utf-8') as f:
        f.write(f"# {skill_data['name']} Skill\n\n{skill_data['description']}\n\n## Tools Required\n")
        for tool in skill_data['tools']:
            f.write(f"- {tool}\n")
    
    # Create dummy script
    with open(f"{skill_dir}/scripts/main.py", 'w', encoding='utf-8') as f:
        f.write(f"#!/usr/bin/env python3\n# Logic for {skill_data['name']}\nprint('Skill running...')\n")
        
    print(f"\n✅ 脚手架已生成至: {skill_dir}/")
    input("\n按回车键继续...")

def run_simulator(skill_data):
    clear_screen()
    display_header()
    print(f"🧪 {skill_data['name']} - 模拟器 (Simulator)")
    print("-" * 60)
    print(f"描述: {skill_data['description']}")
    print(f"加载工具: {', '.join(skill_data['tools'])}")
    print("\n[系统]: 技能逻辑加载成功。请输入指令进行测试。")
    
    while True:
        user_in = input("\n👤 测试输入: ").strip()
        if user_in.lower() in ['exit', 'quit', '0']: break
        
        print("Thinking...", end="", flush=True)
        import time; time.sleep(1)
        print(f"\r🤖 [模拟响应]: 基于工具 {skill_data['tools'][0] if skill_data['tools'] else 'None'}，我将为您执行 '{user_in}'。操作完成！")

    input("\n测试结束，按回车返回...")

def generate_mermaid(skill_data):
    print("\n📊 Mermaid 流程图源码:")
    print("-" * 30)
    mermaid = f"""graph TD
    A[Start] --> B[Check Tools: {', '.join(skill_data['tools'])}]
    B --> C{{Input Valid?}}
    C -- Yes --> D[Execute {skill_data['name']} Logic]
    C -- No --> E[Return Error]
    D --> F[Success Outcome]
    F --> G[End]
    """
    print(mermaid)
    print("-" * 30)
    input("\n按回车返回...")

def main():
    while True:
        clear_screen()
        display_header()
        display_menu()
        choice = input("请输入您的选择 (0-4): ").strip()
        
        if choice == '1':
            concept_guide()
        elif choice == '2':
            skill_builder()
        elif choice == '3':
            export_skills()
        elif choice == '4':
            advanced_menu()
        elif choice == '0':
            print("👋 再见！")
            sys.exit(0)
        else:
            input("❌ 无效选择，按回车重试...")

if __name__ == "__main__":
    main()
