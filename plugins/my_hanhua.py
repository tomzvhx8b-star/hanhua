from pagermaid.listener import listener
from pagermaid.enums import Client, Message

# incoming=True 监听别人发的，outgoing=True 监听自己发的
# filter_not_cmd=True 允许不带逗号前缀触发
@listener(incoming=True, outgoing=True, filter_not_cmd=True)
async def auto_reply_hanhua(message: Message):
    # 如果没文字内容，或者消息里已经包含了这个链接（防止死循环），就跳过
    if not message.text or "setlanguage" in message.text:
        return

    # 匹配关键词
    keywords = ["汉化", "中文包", "语言包", "怎么变中文"]
    
    if any(word in message.text for word in keywords):
        reply_text = (
            "🚀 **极速汉化方案**\n\n"
            "👉 [点击此处：安装简体中文包](https://t.me/setlanguage/zh-hans-raw)\n\n"
            "💡 *提示：点击链接后弹出对话框，选择 Change 即可秒变中文。*"
        )
        try:
            # quote=True 表示回复那条触发的消息
            await message.reply(reply_text, quote=True)
        except:
            pass