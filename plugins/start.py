from pyrogram import Client, Filters
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup




@Client.on_message(Filters.command(["start"]), 1)
async def start (bot, update):

    await bot.send_message(
        chat_id=update.chat.id,
        text=f"Hey 🙋‍♂️{update.from_user.mention} Am YouTube Downloader Bot 😎 I will convert YouTube link to Video / File & MP3..",
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    
                    InlineKeyboardButton("Dev", url="https://t.me/username"),
                    InlineKeyboardButton("Channel", url="https://t.me/username")
                ],
                [
                    InlineKeyboardButton("Help", callback_data="help_menu"),
                    InlineKeyboardButton("Close", callback_data="close_btn")
                ]
            ]
        )
    )



@Client.on_message(Filters.command(["about"]), 1)
async def about(bot, update):

    await bot.send_message(
        chat_id=update.chat.id,
        text= """🙋🏻‍♂️   Hellooo    <code> {}🤓</code>
    
<b>○ My Name :</b> <code>YouTube Downloader Bot</code>
<b>○ Creator :</b> <a href="https://t.me/Physic_hybrid">Physic_Hybrid🇮🇳</a>
<b>○ Credits :</b> <code>Everyone in this journey</code>
<b>○ Language :</b> <code>Python3</code>
<b>○ Library :</b> <a href="https://docs.pyrogram.org/">Pyrogram asyncio 0.17.1</a>
<b>○ Supported Site :</b> <a href="https://www.youtube.com/">Only YouTube</a>
<b>○ Source Code :</b> <a href="https://t.me/AdhavaaBiriyaniKittiyalo">👉 Click Here</a>
<b>○ Server :</b> <a href="https://herokuapp.com/">Heroku</a>
<b>○ Database :</b> <a href="https://www.mongodb.com/">MongoDB</a>
<b>○ Build Status :</b> <code>V2.1 [BETA]</code>
<b>📜 Quote :</b> <code>ആരും പേടിക്കണ്ട എല്ലാവർക്കും കിട്ടും™️</code>""".format(update.from_user.mention),



               
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Close", callback_data="close_btn")
                ]
            ]
        )
    )




@Client.on_callback_query(Filters.regex(r"help_menu"), 2)
async def help_cb(bot, update):
      
      await update.message.edit_text(
           text="help no one help you",
           parse_mode="html",
           reply_markup=InlineKeyboardMarkup(
              [
                  [
                      InlineKeyboardButton("About", callback_data="about_menu"),
                      InlineKeyboardButton("Close", callback_data="close_btn")
                  ]
              ]
            )

      )



@Client.on_callback_query(Filters.regex(r"about_menu"), 2)
async def about_cb(bot, update):
      
      await update.message.edit_text(
           text="about text",
           parse_mode="html",
           reply_markup=InlineKeyboardMarkup(
              [
                  [
                      InlineKeyboardButton("Close", callback_data="close_btn")
                  ]
              ]
            )

      )


@Client.on_callback_query(Filters.regex(r"close_btn"), 2)
async def close_btn_cb(bot, update):
      
      await update.message.delete()
