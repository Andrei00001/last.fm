import uuid
from datetime import datetime

from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from connection_db import async_session
from database.models import User
from repositories.db_repositories import AuthRepositories


async def start_bot(message: types.Message):
    await add_user(message.chat.id)
    url = AuthRepositories.auth_url

    inf = InlineKeyboardButton(text="Авторизация", url=url)
    kb_auth = InlineKeyboardMarkup(resize_keyboard=True)
    kb_auth.add(inf)
    await message.answer("Добро пожаловать\n"
                         "Авторизуйтесь на сайте\n"
                         "После чего вернитесь в бот", reply_markup=kb_auth)


async def add_user(id_telegram):
    user = User(
        id=str(uuid.uuid4()),
        name="",
        id_telegram=id_telegram,
        data_reg=datetime.now(),
        token="",
        session_token="",
        last_auth=datetime.now()
    )

    AuthRepositories.auth(uuid=user.id)
    async with async_session() as session:
        session.add(user)
        await session.commit()
        await session.close()
