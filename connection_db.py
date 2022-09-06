from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from repositories import sql_requests

Base = declarative_base()
engine = sql_requests.DBRepositories.base_config()[0]
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
