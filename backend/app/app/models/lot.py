import enum
from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.schemas.fruit import Fruit

if TYPE_CHECKING:
    from .lot import Lot  # noqa: F401

class Lot(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fruit_id = Column(Integer, ForeignKey("FRUIT.id"))
    fruit = relationship("Fruit", back_populates="lots")
