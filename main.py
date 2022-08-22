from aiogram import Dispatcher
from aiogram.utils import executor
from fastapi import FastAPI

from app_telegram.echo import echo
from connection_bot import dp

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def handlers(dp: Dispatcher):
    dp.register_message_handler(echo, commands=["start"])


if __name__ == "__main__":
    handlers(dp)
    executor.start_polling(dp, skip_updates=True)
