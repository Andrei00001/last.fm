import os
from pathlib import Path

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

token = os.getenv('TOKEN')
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
