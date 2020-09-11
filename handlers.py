from main import bot, dp
import requests

from aiogram.types import Message, CallbackQuery
from config import admin_id
# from keyboards import digitals, summa
import keyboards as kb
from aiogram.dispatcher.filters import Command


# async def send_to_admin(dp):
#     await bot.send_message(chat_id=admin_id, text="Бот запущен")


async def keyboard(dp):
    await bot.send_message(chat_id=admin_id, text="Привет", reply_markup=kb.digitals)


@dp.callback_query_handler(lambda call: True)
async def digit_press(callback_query: CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'нажата кнопка {callback_query["data"]}')


# @dp.callback_query_handler(lambda call: True)
# async def summa(callback_query: CallbackQuery):
#
#         if callback_query["data"]
