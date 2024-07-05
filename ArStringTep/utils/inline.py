from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="- بـدء استخـراج الجلسـة .", callback_data="getsession")],
        [
            InlineKeyboardButton(text="- قنـاة الشـروحـات .", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="مطور البـوت", url="https://t.me/XXXWR"
            ),
        ],
    ]
)

string_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text=" ", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايـروجرام ", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثـون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="إعـادة المحاولـة .", callback_data="getsession")]]
)
