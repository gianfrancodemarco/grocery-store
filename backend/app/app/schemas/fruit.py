from typing import Optional

from app.enums.peel_type_enum import PeelTypeEnum
from pydantic import BaseModel


# Shared properties
class FruitBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    peel_type: Optional[str] = None
    maximum_stationary_time: Optional[int] = None


# Properties to receive on fruit creation
class FruitCreate(FruitBase):
    name: str
    peel_type: str
    maximum_stationary_time: Optional[int] = None

# Properties to receive on fruit update
class FruitUpdate(FruitBase):
    pass


# Properties shared by models stored in DB
class FruitInDBBase(FruitBase):
    id: int
    name: str
    peel_type: PeelTypeEnum
    maximum_stationary_time: int

    class Config:
        orm_mode = True


# Properties to return to client
class Fruit(FruitInDBBase):
    pass


# Properties properties stored in DB
class FruitInDB(FruitInDBBase):
    pass
