from bot import studybot
import logging
from pyrogram import filters

logging.basicConfig(level=logging.INFO)

@studybot.on_message(filters.private & filters.command("/start"))
async def startmsg(client,message):
  await message.reply_text("Hi")
