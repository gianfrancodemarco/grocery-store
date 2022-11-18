import enum
from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.enums.peel_type_enum import PeelTypeEnum
from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .fruit import Lot  # noqa: F401

class Lot(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fruit_id = Column(Integer, ForeignKey("FRUIT.id"))
    parent = relationship("Fruit", back_populates="children")
