from connection_db import Base
from sqlalchemy import Column, Integer, String, DateTime


# Чисто для теста

class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    id_telegram = Column('telegram_id', Integer, nullable=False)
    data_reg = Column('date_reg', DateTime, nullable=False)
    token = Column('token_fm', String, nullable=False)
    last_auth = Column('last_auth', DateTime, nullable=False)

    def __repr__(self):
        return "".format(self.code)
