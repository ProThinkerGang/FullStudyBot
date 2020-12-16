from pyrogram import filters, Client

@Client.on_message(filters.command("/bye") & filters.private)
async def ssss(client,message):
    await message.reply_text("Bye")
