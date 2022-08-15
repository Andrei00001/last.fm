from connection_db import Base
from sqlalchemy import Column, Integer, String

# Чисто для теста
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    user = Column('user', String)

    def __repr__(self):
        return "".format(self.code)
