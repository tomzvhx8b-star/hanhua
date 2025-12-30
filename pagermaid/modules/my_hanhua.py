from pagermaid.listener import listener

# ================= 配置区域 =================
STUDIO_NAME = "极速汉化" 
# ===========================================

# 全自动监听：只要别人发“汉化”、“中文”等词，机器人秒回链接
@listener(is_plugin=True, incoming=True, outgoing=True, pattern=".*(汉化|中文包).*")
async def auto_reply(message):
    # 排除掉自己发的广告，防止无限循环
    if "setlanguage" in message.text:
        return
    
    clean_text = (
        f"🚀 **{STUDIO_NAME} 一键汉化方案**\n\n"
        "👉 [点击此处：安装简体中文包](https://t.me/setlanguage/zh-hans-raw)\n\n"
        "💡 *提示：点击链接后弹出对话框，选择 Change 即可秒变中文。*"
    )
    await message.reply(clean_text)