from pagermaid.listener import listener

@listener(command="hanhua",
          description="发送一键汉化链接")
async def hanhua_link(message):
    # 这里你可以修改你想要的文案
    text = (
        "🚀 **Telegram 一键汉化方案**\n\n"
        "点击下方链接即可安装中文语言包：\n"
        "🔹 [点击这里：一键安装简体中文](https://t.me/setlanguage/zh-hans-raw)\n\n"
        "💡 提示：点击后在弹出的窗口选择 'Change' 或 '更改' 即可。"
    )
    await message.edit(text)

@listener(is_plugin=True, outgoing=True, pattern=".*(怎么汉化|汉化包|中文包).*")
async def auto_hanhua(message):
    """当你在群里提到这些词时，自动提醒"""
    await message.reply("需要汉化吗？点击这个链接：https://t.me/setlanguage/zh-hans-raw")