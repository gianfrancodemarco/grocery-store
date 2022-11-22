from datetime import datetime
from typing import Optional

from app.enums.fruit_size_enum import FruitSizeEnum
from pydantic import BaseModel

# Shared properties
class SensorBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    fruit_size: Optional[str] = None
    medium_energy_consumption: Optional[float] = None
    cost: Optional[float] = None
    brand: Optional[str] = None


# Properties to receive on fruit creation
class SensorCreate(SensorBase):
    name: str = None
    fruit_size: str = None
    medium_energy_consumption: Optional[float] = None
    cost: Optional[float] = None
    brand: Optional[str] = None


# Properties to receive on fruit update
class SensorUpdate(SensorBase):
    id: int = None

# Properties shared by models stored in DB
class SensorInDBBase(SensorBase):
    id: int
    name: str
    fruit_size: FruitSizeEnum 
    medium_energy_consumption: float
    cost: float
    brand: str = None

    class Config:
        orm_mode = True


# Properties to return to client
class Sensor(SensorInDBBase):
    pass


# Properties properties stored in DB
class SensorInDB(SensorInDBBase):
    pass