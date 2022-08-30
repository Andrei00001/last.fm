from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from repositories.db_repositories import DBRepositories

Base = declarative_base()
engine = DBRepositories.base_config()[0]
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
