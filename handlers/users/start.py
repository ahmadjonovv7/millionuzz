from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart


from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.million import million_buttons
from keyboards.default.bravo import bravo_buttons
from keyboards.default.dizayin import dizayin_buttons

from loader import dp,bot



from data.config import ADMINS
from keyboards.inline.menu_panel import kb
from loader import dp,db


@dp.message_handler(commands='obunachilar',chat_id ='1358690178')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    try:
        db.add_user(user_id=user_id)
    except:
        pass
    await message.answer(f"Obunachilar statikasi 📊, {message.from_user.full_name}!",reply_markup=kb.menuus())


@dp.callback_query_handler(text="stat")
async def Admin_send(call: types.CallbackQuery):
    statiska = db.stat()
    for x in statiska:
        await call.message.answer(f"Bot foidalanuvchilari <b>{x} nafar</b>")



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum siz bu yerda                                                                                          MILLION DIZAYIN BRAVO KONSERTLARINI topishingiz mumukin👇",reply_markup=menu_buttons)



@dp.message_handler(text='Million konserti')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang👇",reply_markup=million_buttons)


@dp.message_handler(text='Bravo konserti')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang👇",reply_markup=bravo_buttons)


@dp.message_handler(text='Dizayin konserti')
async def bot_start(message: types.Message, keys=None):
    await message.answer(f"Tanlang👇",reply_markup=dizayin_buttons)


@dp.message_handler(commands='reklama', chat_id ='1358690178')
async def bot_start(message: types.Message):
    userlar = db.select_barch_foydalanuvchilar()
    print(userlar)
    for user in userlar:
        await bot.send_photo(chat_id=user[1],photo='https://t.me/UstozShogird/26311',caption='salom')