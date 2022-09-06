import os
from pathlib import Path

from aiogram import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from app_telegram.handlers import start_bot, get_trek, auth
from connection_bot import dp
from repositories.sql_requests import SQLRepositories

from repositories.url_requests import AuthRepositories

app = FastAPI()

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
bot_token = os.getenv('TOKEN')


@app.get("/{uuid}")
async def root(uuid, token):
    session_data = AuthRepositories.session(token)
    await SQLRepositories.update_user_token(uuid, token, session_data)
    return HTMLResponse(
        "<b>Hello world</b>"'<a href="https://t.me/LastFm_Project_bot"><input type="button" value="Вернуться к боту" > </a>')


def handlers(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=["start"])
    dp.register_message_handler(auth, regexp="Авторизация")
    dp.register_message_handler(get_trek, regexp="Текущий трек")


if __name__ == "__main__":
    handlers(dp)
    executor.start_polling(dp, skip_updates=True)


# text = "Вы успешно авторизованы"
# requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id_telegram}&text={text}")
