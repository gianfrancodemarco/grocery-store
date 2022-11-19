from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import ARRAY
from .allergies_fruits import allergies_fruits

if TYPE_CHECKING:
    from .allergy import Allergy  # noqa: F401

class Allergy(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    symptoms = Column(String(1000))
    
    fruits = relationship(
        "Fruit", secondary=allergies_fruits, back_populates="allergies"
    )