from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from repositories.url_requests import AuthRepositories


auth = KeyboardButton(text="Авторизация")
kb_auth = ReplyKeyboardMarkup(resize_keyboard=True)
kb_auth.add(auth)


url = AuthRepositories.auth_url
auth_url = InlineKeyboardButton(text="Авторизация", url=url)
kb_auth_url = InlineKeyboardMarkup(resize_keyboard=True)
kb_auth_url.add(auth_url)

trek = KeyboardButton(text="Текущий трек")
kb_trek = ReplyKeyboardMarkup(resize_keyboard=True)
kb_trek.add(trek)
