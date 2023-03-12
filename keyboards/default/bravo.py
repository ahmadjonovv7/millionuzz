from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

bravo_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bravo 2021"),
            KeyboardButton(text="Bravo 2019")
        ],
        [
            KeyboardButton(text="Bravo 2018"),
            KeyboardButton(text="BRAVO JAMOASI AMERIKADAGI KONSERTI")
        ]
    ],
    resize_keyboard=True
)