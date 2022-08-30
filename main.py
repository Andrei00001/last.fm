import os
from pathlib import Path

from aiogram import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import update

from app_telegram.handlers import start_bot
from connection_bot import dp
from connection_db import async_session
from database.models import User
from repositories.db_repositories import AuthRepositories

app = FastAPI()

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
bot_token = os.getenv('TOKEN')


@app.get("/{uuid}")
async def root(uuid, token):
    session_data = AuthRepositories.session(token)
    await update_user_token(uuid, token, session_data)
    # text = "Вы успешно авторизованы"
    # requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id_telegram}&text={text}")
    return HTMLResponse(
        "<b>Hello world</b>"'<a href="https://t.me/LastFm_Project_bot"><input type="button" value="Вернуться к боту" > </a>')


async def update_user_token(uuid, token, session_data):
    async with async_session() as session:
        query = update(
            User
        ).where(
            User.id == uuid
        ).values(
            token=token,
            name=session_data["name"],
            session_token=session_data['key'],
        ).execution_options(
            synchronize_session="fetch"
        )
        await session.execute(query)
        await session.commit()


def handlers(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=["start"])


if __name__ == "__main__":
    handlers(dp)
    executor.start_polling(dp, skip_updates=True)
