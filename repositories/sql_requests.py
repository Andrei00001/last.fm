import os
import uuid
from datetime import datetime

from connection_db import async_session
from database.models import User
from sqlalchemy import update, select

from repositories.url_requests import AuthRepositories
from sqlalchemy.ext.asyncio import create_async_engine


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


class SQLRepositories:

    @classmethod
    async def update_user_token(cls, uuid, token, session_data):
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

    @classmethod
    async def add_user(cls, id_telegram):
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

    @classmethod
    async def get_username(cls, id_telegram):
        async with async_session() as session:
            query = select(
                User
            ).where(
                User.id_telegram == id_telegram
            )
            user = await session.execute(query)
            user = [i.name for i in user.scalars()][0]
            return user
