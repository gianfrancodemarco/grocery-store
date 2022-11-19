from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .recipes_fruits import recipes_fruits

if TYPE_CHECKING:
    from .recipe import Recipe  # noqa: F401

class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    symptoms = Column(String(1000))
    
    fruits = relationship(
        "Fruit", secondary=recipes_fruits, back_populates="recipes"
    )