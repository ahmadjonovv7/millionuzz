from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

million_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Million 2022 Kuz 4K")
        ],
        [
            KeyboardButton(text="Million 2022"),
            KeyboardButton(text="Million 2021")
        ],
        [
            KeyboardButton(text="Million 2021 Kuz"),
            KeyboardButton(text="Million 2020")
        ],
        [
            KeyboardButton(text="Million 2019"),
            KeyboardButton(text="Million 2018")
        ],
        [
            KeyboardButton(text="Million 2017"),
            KeyboardButton(text="Million 2016")
        ],
        [
            KeyboardButton(text="Million 2014"),
            KeyboardButton(text="Million 2012")
        ]
    ],
    resize_keyboard=True
)