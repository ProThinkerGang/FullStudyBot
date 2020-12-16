import logging
import asyncio as ae
from telethon.sync import TelegramClient
from telethon import events
from Var import var

studybot = TelegramClient("Study Bot",api_id=var.API_ID,api_hash=var.API_HASH).start(bot_token=var.BOT_TOKEN)

with studybot:
    studybot.run_until_disconnected()
