from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.allergy import Allergy
from app.models.fruit import Fruit
from app.schemas.allergy import AllergyCreate, AllergyUpdate
from sqlalchemy.orm import Session


class CRUDAllergy(CRUDBase[Allergy, AllergyCreate, AllergyUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Allergy]:
        return db.query(Allergy).filter(Allergy.name == name).first()

    def create(self, db: Session, *, obj_in: AllergyCreate) -> Allergy:
        db_obj = Allergy(
            name=obj_in.name,
            symptoms=obj_in.symptoms
        )
        db_obj.fruits = db.query(Fruit).filter(Fruit.id.in_(obj_in.fruits)).all()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Allergy, obj_in: Union[AllergyUpdate, Dict[str, Any]]
    ) -> Allergy:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        for fruit in db_obj.fruits:
            if fruit.id not in update_data['fruits']:
                db_obj.fruits.remove(fruit)

        update_data['fruits'] = db.query(Fruit).filter(Fruit.id.in_(obj_in.fruits)).all()
        return super().update(db, db_obj=db_obj, obj_in=update_data)

allergy = CRUDAllergy(Allergy)
