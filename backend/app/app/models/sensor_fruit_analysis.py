from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.schemas.lot import Lot
from app.schemas.sensor import Sensor
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint

if TYPE_CHECKING:
    from .sensor_fruit_analysis import SensorFruitAnalysis  # noqa: F401

class SensorFruitAnalysis(Base):
    __tablename__: str = "SENSOR_FRUIT_ANALYSIS"
    
    id = Column(Integer, primary_key=True, index=True)
    lot_id = Column(ForeignKey("LOT.id"))
    sensor_id = Column(ForeignKey("SENSOR.id"))
    description = Column(String(1000))
    UniqueConstraint('sensor_id', 'lot_id')