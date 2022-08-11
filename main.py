from aiogram import Dispatcher
from aiogram.utils import executor

from app.echo import echo
from connection_bot import dp


def start_handlers(dp: Dispatcher):
    dp.register_message_handler(echo, commands=["start"])


start_handlers(dp)

executor.start_polling(dp, skip_updates=True)