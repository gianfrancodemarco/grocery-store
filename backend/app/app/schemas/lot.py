from typing import Optional

from app.schemas.fruit import Fruit
from pydantic import BaseModel


# Shared properties
class LotBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    fruit_id: Optional[int] = None
    fruit: Optional[Fruit] = None

# Properties to receive on fruit creation
class LotCreate(LotBase):
    name: str
    fruit_id: int


# Properties to receive on fruit update
class LotUpdate(LotBase):
    id: int = None


# Properties shared by models stored in DB
class LotInDBBase(LotBase):
    id: int
    name: str
    fruit_id: int
    fruit: Fruit

    class Config:
        orm_mode = True


# Properties to return to client
class Lot(LotInDBBase):
    pass


# Properties properties stored in DB
class LotInDB(LotInDBBase):
    pass
