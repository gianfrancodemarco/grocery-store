from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.schemas.lot import Lot
from app.schemas.sensor import Sensor
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint

if TYPE_CHECKING:
    from .sensor_fruit_analysis import SensorFruitAnalysis  # noqa: F401

class SensorFruitAnalysis(Base):
    __table_args__ = (
        # this can be db.PrimaryKeyConstraint if you want it to be a primary key
        UniqueConstraint('sensor_id', 'lot_id'),
    )
    id = Column(Integer, primary_key=True, index=True)
    lot_id = Column(ForeignKey("LOT.id"), primary_key=True),
    sensor_id = Column(ForeignKey("SENSOR.id"), primary_key=True),
    description = Column(String(1000))