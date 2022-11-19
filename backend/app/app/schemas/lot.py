from typing import Optional

from app.enums.peel_type_enum import PeelTypeEnum
from pydantic import BaseModel


# Shared properties
class LotBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    fruit_id: Optional[int] = None


# Properties to receive on fruit creation
class LotCreate(LotBase):
    name: str
    fruit_id: int


# Properties to receive on fruit update
class LotUpdate(LotBase):
    pass


# Properties shared by models stored in DB
class LotInDBBase(LotBase):
    id: int
    name: str
    fruit_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Lot(LotInDBBase):
    pass


# Properties properties stored in DB
class LotInDB(LotInDBBase):
    pass
