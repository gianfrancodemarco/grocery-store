from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.enums.recipe_budget_enum import RecipeBudgetEnum
from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from .recipes_fruits import recipes_fruits

if TYPE_CHECKING:
    from .recipe import Recipe  # noqa: F401

class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(1000))
    budget = Column(
        Enum(RecipeBudgetEnum, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
        default=RecipeBudgetEnum.MEDIUM.value,
        server_default=RecipeBudgetEnum.MEDIUM.value
    )
    fruits = relationship(
        "Fruit", secondary=recipes_fruits, back_populates="recipes"
    )