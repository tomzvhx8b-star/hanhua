from pagermaid.listener import listener
from pagermaid.utils import alias_command

@listener(command="hanhua",
          description="发送一键汉化链接")
async def hanhua_link(message):
    text = "🚀 **点击一键汉化：** [点击安装](https://t.me/setlanguage/zh-hans-raw)"
    await message.edit(text)

@listener(is_plugin=True, outgoing=True, pattern=".*(汉化|中文包).*")
async def auto_hanhua(message):
    await message.reply("需要汉化？点击这里：https://t.me/setlanguage/zh-hans-raw")