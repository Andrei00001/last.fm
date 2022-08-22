from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    id_telegram: int
    data_reg: datetime
    token: str
    last_auth: datetime
