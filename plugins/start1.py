from pyrogram import filters, Client
from bot import studybot

@Client.on_message(filters.command("/bye") & filters.private)
async def ssss(client,message):
    await message.reply_text("Bye")
