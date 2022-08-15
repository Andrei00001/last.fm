from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from repositories.db_repositories import DBRepositories

Base = declarative_base()
engine = DBRepositories.base_config()
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)




