from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="- بـدء استخـراج الجلسـة .", callback_data="getsession")],
        [
            InlineKeyboardButton(text="- قنـاة الشـروحـات .", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="مطور البـوت", url="https://t.me/@X_wwr"
            ),
        ],
    ]
)

string_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="تليثـون", callback_data="telethon")
        ],
        [InlineKeyboardButton(text="بايـروجرام ", callback_data="pyrogram"),],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="إعـادة المحاولـة .", callback_data="getsession")]]
)
