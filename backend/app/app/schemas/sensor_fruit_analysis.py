from datetime import datetime
from typing import Optional

from app.schemas.lot import Lot
from app.schemas.sensor import Sensor
from pydantic import BaseModel

# Shared properties
class SensorFruitAnalysisBase(BaseModel):
    id: Optional[int] = None
    description: Optional[str] = None

    sensor_id: int = None
    sensor: Optional[Sensor] = None

    lot_id: int = None
    lot: Optional[Lot] = None

# Properties to receive on lot creation
class SensorFruitAnalysisCreate(SensorFruitAnalysisBase):
    sensor_id: int
    lot_id: int

# Properties to receive on lot update
class SensorFruitAnalysisUpdate(SensorFruitAnalysisBase):
    id: int = None

# Properties shared by models stored in DB
class SensorFruitAnalysisInDBBase(SensorFruitAnalysisBase):
    id: int
    description: str
    sensor_id: int 
    lot_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class SensorFruitAnalysis(SensorFruitAnalysisInDBBase):
    pass


# Properties properties stored in DB
class SensorFruitAnalysisInDB(SensorFruitAnalysisInDBBase):
    pass