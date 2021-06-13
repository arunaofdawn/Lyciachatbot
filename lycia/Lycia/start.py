from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
Haloo.. Nama saya Rese休憩, Selain pandai bernyanyi dan mengelola grup saya juga pandai ngebacot! Silahkan tambahkan saya ke grup..daripada TMO ujung"nya cuma disetan mending ngebacot ama gua kan!
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Support 📢", url = "https://t.me/arunasupportbot"), InlineKeyboardButton("Owner 🙇‍♂", url = "https://t.me/RosoOwner_bot")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
