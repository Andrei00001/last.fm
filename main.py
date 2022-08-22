from threading import Thread

from aiogram import Dispatcher
from aiogram.utils import executor
import asyncio
from app.echo import echo
from connection_bot import dp
from connection_db import Base, engine
from database.models import User


def handlers(dp: Dispatcher):
    dp.register_message_handler(echo, commands=["start"])


if __name__ == "__main__":

    handlers(dp)
    executor.start_polling(dp, skip_updates=True)


