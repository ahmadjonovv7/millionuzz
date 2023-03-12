from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Million konserti"),
            KeyboardButton(text="Dizayin konserti")
        ],
        [
            KeyboardButton(text="Bravo konserti")
        ]
    ],
    resize_keyboard=True
)