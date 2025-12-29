#!/usr/bin/env python3
"""
一键汉化脚本 - PagerMaid-Pyro
用法: python install_zh.py
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime


def print_step(step_num, message):
    print(f"\n[{step_num}] {message}")
    print("-" * 50)


def print_success(message):
    print(f"✅ {message}")


def print_error(message):
    print(f"❌ {message}")


def print_info(message):
    print(f"ℹ️  {message}")


def get_script_directory():
    """获取脚本所在目录"""
    return Path(__file__).parent.resolve()


def backup_file(file_path):
    """备份文件"""
    if file_path.exists():
        backup_path = file_path.with_suffix(f".bak.{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        shutil.copy2(file_path, backup_path)
        print_info(f"已备份: {file_path.name} -> {backup_path.name}")
        return backup_path
    return None


def copy_language_file(src_lang_dir, dst_lang_dir):
    """复制汉化语言文件"""
    print_step(1, "正在应用中文语言文件...")
    
    src_zh_cn = src_lang_dir / "zh-cn.yml"
    dst_zh_cn = dst_lang_dir / "zh-cn.yml"
    
    if not src_zh_cn.exists():
        print_error(f"源语言文件不存在: {src_zh_cn}")
        return False
    
    if not dst_lang_dir.exists():
        print_error(f"目标语言目录不存在: {dst_lang_dir}")
        return False
    
    if dst_zh_cn.exists():
        backup_file(dst_zh_cn)
    
    shutil.copy2(src_zh_cn, dst_zh_cn)
    print_success(f"已安装中文语言文件: {dst_zh_cn}")
    return True


def copy_module_files(src_modules_dir, dst_modules_dir):
    """复制汉化后的模块文件"""
    print_step(2, "正在应用汉化模块文件...")
    
    if not src_modules_dir.exists():
        print_error(f"源模块目录不存在: {src_modules_dir}")
        return False
    
    if not dst_modules_dir.exists():
        print_error(f"目标模块目录不存在: {dst_modules_dir}")
        return False
    
    modified_files = []
    new_files = []
    
    src_files = list(src_modules_dir.glob("*.py"))
    for src_file in src_files:
        dst_file = dst_modules_dir / src_file.name
        
        if dst_file.exists():
            backup_file(dst_file)
            shutil.copy2(src_file, dst_file)
            modified_files.append(src_file.name)
        else:
            shutil.copy2(src_file, dst_file)
            new_files.append(src_file.name)
            print_success(f"已安装新模块: {src_file.name}")
    
    for name in modified_files:
        print_success(f"已更新模块: {name}")
    
    if modified_files:
        print_info(f"共更新 {len(modified_files)} 个模块文件")
    if new_files:
        print_info(f"共安装 {len(new_files)} 个新模块文件")
    
    if "hanhua" in new_files:
        print_info("✨ 新功能: hanhua 命令已安装")
        print_info("   使用 ,hanhua 命令可查看汉化信息")
    
    return True


def update_config_language(config_path):
    """更新配置文件为中文"""
    print_step(3, "正在配置默认语言为中文...")
    
    if not config_path.exists():
        print_error(f"配置文件不存在: {config_path}")
        return False
    
    backup_file(config_path)
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        original_content = content
        
        content = content.replace(
            'application_language: "en"',
            'application_language: "zh-cn"'
        )
        content = content.replace(
            "application_language: 'en'",
            "application_language: 'zh-cn'"
        )
        
        if 'application_language: "zh-cn"' not in content and \
           "application_language: 'zh-cn'" not in content:
            content = content.replace(
                "application_language:",
                'application_language: "zh-cn"  # 设置为中文',
                1
            )
        
        if content != original_content:
            with open(config_path, "w", encoding="utf-8") as f:
                f.write(content)
            print_success("已配置默认语言为中文 (zh-cn)")
        else:
            print_info("语言配置已经是中文，无需修改")
        
        return True
    except Exception as e:
        print_error(f"配置更新失败: {e}")
        return False


def update_api_credentials(config_path):
    """更新 API 凭证为预设值（硬编码）"""
    print_step(4, "正在配置 API 凭证...")
    
    if not config_path.exists():
        print_error(f"配置文件不存在: {config_path}")
        return False
    
    backup_file(config_path)
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        original_content = content
        
        API_ID = "21724"
        API_HASH = "3e0cb5efcd52300aec5994fdfc5bdc16"
        
        content = content.replace('api_id: "ID_HERE"', f'api_id: "{API_ID}"')
        content = content.replace('api_hash: "HASH_HERE"', f'api_hash: "{API_HASH}"')
        
        if content != original_content:
            with open(config_path, "w", encoding="utf-8") as f:
                f.write(content)
            print_success(f"已配置 API 凭证 (ID: {API_ID})")
        else:
            print_info("API 凭证已配置，无需修改")
        
        return True
    except Exception as e:
        print_error(f"API 凭证配置失败: {e}")
        return False


def copy_web_html_files(src_web_dir, dst_web_dir):
    """复制汉化后的 Web 界面文件"""
    print_step(4, "正在应用汉化 Web 界面文件...")
    
    if not src_web_dir.exists():
        print_error(f"源 Web 目录不存在: {src_web_dir}")
        return False
    
    if not dst_web_dir.exists():
        print_error(f"目标 Web 目录不存在: {dst_web_dir}")
        return False
    
    src_html_dir = src_web_dir / "html"
    dst_html_dir = dst_web_dir / "html"
    
    if not src_html_dir.exists():
        print_info(f"源 HTML 目录不存在，跳过: {src_html_dir}")
        return True
    
    modified_files = []
    
    html_files = list(src_html_dir.glob("*.html"))
    for src_file in html_files:
        dst_file = dst_html_dir / src_file.name
        
        if dst_file.exists():
            backup_file(dst_file)
        
        shutil.copy2(src_file, dst_file)
        modified_files.append(src_file.name)
        print_success(f"已更新 Web 界面: {src_file.name}")
    
    if modified_files:
        print_info(f"共更新 {len(modified_files)} 个 Web 界面文件")
    
    return True


def main():
    print("\n" + "=" * 60)
    print("  PagerMaid-Pyro 一键汉化脚本")
    print("  One-Click Chinese Localization Script")
    print("=" * 60)
    
    script_dir = get_script_directory()
    project_root = script_dir.parent
    
    print_info(f"脚本目录: {script_dir}")
    print_info(f"项目目录: {project_root}")
    
    src_lang_dir = script_dir / "languages" / "built-in"
    src_modules_dir = script_dir / "pagermaid" / "modules"
    src_web_dir = script_dir / "pagermaid" / "web"
    
    dst_lang_dir = project_root / "languages" / "built-in"
    dst_modules_dir = project_root / "pagermaid" / "modules"
    dst_web_dir = project_root / "pagermaid" / "web"
    config_path = project_root / "data" / "config.yml"
    
    all_success = True
    
    if src_lang_dir.exists():
        if not copy_language_file(src_lang_dir, dst_lang_dir):
            all_success = False
    else:
        print_info("跳过语言文件安装（源目录不存在）")
    
    if src_modules_dir.exists():
        if not copy_module_files(src_modules_dir, dst_modules_dir):
            all_success = False
    else:
        print_info("跳过模块文件安装（源目录不存在）")
    
    if src_web_dir.exists():
        if not copy_web_html_files(src_web_dir, dst_web_dir):
            all_success = False
    else:
        print_info("跳过 Web 界面文件安装（源目录不存在）")
    
    if config_path.exists():
        if not update_config_language(config_path):
            all_success = False
    else:
        print_info("跳过配置更新（配置文件不存在，将使用默认配置）")
    
    if config_path.exists():
        if not update_api_credentials(config_path):
            all_success = False
    else:
        print_info("跳过 API 凭证配置（配置文件不存在）")
    
    print("\n" + "=" * 60)
    if all_success:
        print("✅ 汉化安装完成！")
        print("\n下一步操作:")
        print("  1. 重启 PagerMaid-Pyro 服务")
        print("  2. 机器人将以中文界面运行")
        print("\n如果遇到问题，备份文件已保存在 data 目录下（.bak.时间戳 格式）")
    else:
        print("⚠️  部分安装步骤遇到问题，请检查上方错误信息")
        print("备份文件已保存在 data 目录下（.bak.时间戳 格式）")
    print("=" * 60 + "\n")
    
    return 0 if all_success else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n操作被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
