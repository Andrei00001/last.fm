
from pprint import pprint

from aiogram import types

from app_telegram.keyboards import kb_auth, kb_auth_url, kb_trek
from repositories.url_requests import AuthRepositories
from repositories.sql_requests import SQLRepositories


async def start_bot(message: types.Message):
    await SQLRepositories.add_user(message.chat.id)
    await message.answer("Добро пожаловать", reply_markup=kb_auth)


async def auth(message: types.Message):
    await message.answer("Авторизуйтесь на сайте\n"
                         "После чего вернитесь в бот", reply_markup=kb_auth_url)
    await message.answer("Для получения текущей песни нажмите ниже", reply_markup=kb_trek)


async def get_trek(message: types.Message):
    username = await SQLRepositories.get_username(message.chat.id)
    trek_data = AuthRepositories.request_trek(username)
    pprint(trek_data)
    await message.answer(f"Артист: {trek_data['artist']['#text']}\nИмя трека: {trek_data['name']}\n{trek_data['url']}")
