from pyrogram import CLient, Filters
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup




@Client.on_message(Filters.command(["start"]), 1)
async def start (bot, update):

    await bot.send_message(
        chat_id=update.chat.id,
        text="start msg",
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    
                    InlineKeyboardButton("Dev", url="https://t.me/username"),
                    InlineKeyboardButton("Channel", url="https://t.me/username")
                ],
                [
                    InlineKeyboardButton("Help", callback="help_menu"),
                    InlineKeyboardButton("Close", callback="close_btn")
                ]
            ]
        )
    )



@Client.on_message(Filters.command(["about"]), 1)
async def about(bot, update):

    await bot.send_message(
        chat_id=update.chat.id,
        text="about msg",
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Close", callback="close_btn")
                ]
            ]
        )
    )




@Client.on_callback_query(Filters.regex(r"help_menu"), 2)
async def help_cb(bot, update):
      
      await update.message.edit_text(
           text="help text",
           parse_mode="html",
           reply_markup=InlineKeyboardMarkup(
              [
                  [
                      InlineKeyboardButton("About", callback="about_menu"),
                      InlineKeyboardButton("Close", callback="close_btn")
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
                      InlineKeyboardButton("Close", callback="close_btn")
                  ]
              ]
            )

      )


@Client.on_callback_query(Filters.regex(r"close_btn"), 2)
async def close_btn_cb(bot, update):
      
      await update.message.delete()
