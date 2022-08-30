import hashlib
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class DBRepositories:

    @staticmethod
    def base_config(
            dialect: str = "postgresql",
            driver: str = "asyncpg",
            username: str = os.getenv('USERNAME'),
            password: str = os.getenv('PASSWORD'),
            host: str = "localhost",
            port: str = "5432",
            database_name: str = "last_fm",
            echo: bool = True,
            pool_size: int = 10,
            max_overflow: int = 100,
            encoding: str = "utf8",
    ):
        connect_args: dict = {"server_settings": {"jit": "off"}}
        return create_async_engine(
            f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database_name}",
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
            encoding=encoding,
            connect_args=connect_args
        ), f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database_name}"


class AuthRepositories:
    auth_url = None
    api_key = os.getenv('API_KEY')

    @classmethod
    def auth(cls, uuid):
        url = "http://www.last.fm/api/auth/?api_key="
        cb = f"&cb=http://127.0.0.1:8000/{uuid}/"
        cls.auth_url = url+cls.api_key+cb

    @classmethod
    def session(cls, token):
        hash = cls.hash(token)
        response = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=auth.getSession&api_key={cls.api_key}&token={token}&api_sig={hash}&format=json")
        data = json.loads(response.text)
        return data['session']

    @classmethod
    def hash(cls, token):
        str = f"api_key{cls.api_key}methodauth.getSessiontoken{token}9d44e96061dd86657ef162463e63fd73"
        return hashlib.md5(str.encode('utf-8')).hexdigest()
