import enum
from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.enums.fruit_size_enum import FruitSizeEnum
from sqlalchemy import Column, Enum, Integer, String, Float

if TYPE_CHECKING:
    from .sensor import Sensor  # noqa: F401

class Sensor(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fruit_size = Column(
        Enum(FruitSizeEnum, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
        default=FruitSizeEnum.MEDIUM.value,
        server_default=FruitSizeEnum.MEDIUM.value
    )
    medium_energy_consumption = Column(Float, server_default="1")
    cost = Column(Float, server_default="50")
    brand = Column(String(100))
