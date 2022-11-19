from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Table, ForeignKey, Column
from app.schemas.fruit import Fruit
from app.schemas.recipe import Recipe

recipes_fruits = Table(
    "RECIPES_FRUITS",
    Base.metadata,
    Column("recipe_id", ForeignKey("RECIPE.id"), primary_key=True),
    Column("fruit_id", ForeignKey("FRUIT.id"), primary_key=True),
)