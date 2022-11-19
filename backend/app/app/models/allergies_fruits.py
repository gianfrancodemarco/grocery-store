from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Table, ForeignKey, Column
from app.schemas.fruit import Fruit
from app.schemas.allergy import Allergy

allergies_fruits = Table(
    "ALLERGIES_FRUITS",
    Base.metadata,
    Column("allergy_id", ForeignKey("ALLERGY.id"), primary_key=True),
    Column("fruit_id", ForeignKey("FRUIT.id"), primary_key=True),
)