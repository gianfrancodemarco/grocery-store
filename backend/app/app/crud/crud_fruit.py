from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.fruit import Fruit
from app.schemas.fruit import FruitCreate, FruitUpdate
from sqlalchemy.orm import Session


class CRUDFruit(CRUDBase[Fruit, FruitCreate, FruitUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Fruit]:
        return db.query(Fruit).filter(Fruit.name == name).first()

    def create(self, db: Session, *, obj_in: FruitCreate) -> Fruit:
        db_obj = Fruit(
            name=obj_in.name,
            peel_type=obj_in.peel_type,
            maximum_stationary_time=obj_in.maximum_stationary_time,
            size=obj_in.size
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Fruit, obj_in: Union[FruitUpdate, Dict[str, Any]]
    ) -> Fruit:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

fruit = CRUDFruit(Fruit)
