from datetime import datetime
from typing import Optional
from google.oauth2.service_account import Credentials
from const import MAX_NAME_LEN
from pydantic import BaseModel, Extra, Field, PositiveInt


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None, max_length=MAX_NAME_LEN)
    description: Optional[str] = Field(None, min_anystr_length=1)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., max_length=MAX_NAME_LEN)
    description: str = Field(..., min_anystr_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
