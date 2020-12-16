from pyrogram import filters
from bot import studybot

@studybot.on_message(filters.command("/bye") & filters.private)
async def ssss(client,message):
    await message.reply_text("Bye")
