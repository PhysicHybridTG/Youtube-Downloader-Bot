from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<code>Click The Help Button And See The Magic..🤡</code>"
    await message.reply_text(helptxt)
