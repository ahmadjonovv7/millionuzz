from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

dizayin_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dizayn 2021"),
            KeyboardButton(text="Dizayn 2020")
        ],
        [
            KeyboardButton(text="Dizayn 2019"),
            KeyboardButton(text="Dizayn 2017")
        ],
        [
            KeyboardButton(text="Dizayn 2016"),
            KeyboardButton(text="Dizayn 2015"),
        ],
        [
            KeyboardButton(text="Dizayn 2014"),
            KeyboardButton(text="Dizayn 2013"),
        ],
        [
            KeyboardButton(text="Dizayn 2012"),
            KeyboardButton(text="Dizayn 2011")
        ]
    ],
    resize_keyboard=True
)