"""PagerMaid module for Chinese localization information."""

from pyrogram.enums import BotCommand

from pagermaid.listener import listener
from pagermaid.utils import lang
from pagermaid.hook import Hook
from pagermaid.enums import Message
from pagermaid.services import bot


@listener(
    is_plugin=False,
    command="hanhua",
    description=lang("hanhua_des"),
)
async def hanhua(message: Message):
    """Show Chinese localization information."""
    await message.edit(lang("hanhua_msg"))


@Hook.on_startup()
async def register_hanhua_commands():
    """Register /hanhua as a bot command."""
    await bot.set_bot_commands(
        [BotCommand(command="hanhua", description=lang("hanhua_des"))]
    )

BRAND_MAINTAINER = "汉化作者"
BRAND_SUPPORT_LINK = "https://t.me/your_support_channel"

async def hanhua_handler(client, message):
    """Telegram bot command handler for /hanhua"""
    await message.reply(lang("hanhua_msg"))
