from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.enums.peel_type_enum import PeelTypeEnum
from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from .allergies_fruits import allergies_fruits
from .recipes_fruits import recipes_fruits

if TYPE_CHECKING:
    from .fruit import Fruit  # noqa: F401

class Fruit(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    peel_type = Column(
        Enum(PeelTypeEnum, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
        default=PeelTypeEnum.EDIBLE.value,
        server_default=PeelTypeEnum.EDIBLE.value
    )
    maximum_stationary_time = Column(Integer, server_default="24")

    lots = relationship("Lot")
    allergies = relationship(
        "Allergy", secondary=allergies_fruits, back_populates="fruits"
    )
    recipes = relationship(
        "Recipe", secondary=recipes_fruits, back_populates="fruits"
    )