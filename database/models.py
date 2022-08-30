
from connection_db import Base
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    id_telegram = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    data_reg = Column(DateTime, nullable=False)
    token = Column(String, nullable=False)
    session_token = Column(String, nullable=False)
    last_auth = Column(DateTime, nullable=False)

    def __repr__(self):
        return "".format(self.code)
