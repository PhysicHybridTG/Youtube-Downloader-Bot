from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support Group", url="https://t.me/InFoTel_Group")],
        [InlineKeyboardButton(
            "My Father 👩‍💻", url="https://t.me/Physic_hybrid")]
        
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/Am YouTube Downloader Bot 😎 I will convert YouTube link to Video / File & MP3.."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
