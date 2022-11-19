from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.recipe import Recipe
from app.models.fruit import Fruit
from app.schemas.recipe import RecipeCreate, RecipeUpdate
from sqlalchemy.orm import Session


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Recipe]:
        return db.query(Recipe).filter(Recipe.name == name).first()

    def create(self, db: Session, *, obj_in: RecipeCreate) -> Recipe:
        db_obj = Recipe(
            name=obj_in.name,
            description=obj_in.description
        )
        db_obj.fruits = db.query(Fruit).filter(Fruit.id.in_(obj_in.fruits)).all()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Recipe, obj_in: Union[RecipeUpdate, Dict[str, Any]]
    ) -> Recipe:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        for fruit in db_obj.fruits:
            if fruit.id not in update_data['fruits']:
                db_obj.fruits.remove(fruit)

        update_data['fruits'] = db.query(Fruit).filter(Fruit.id.in_(obj_in.fruits)).all()
        return super().update(db, db_obj=db_obj, obj_in=update_data)

recipe = CRUDRecipe(Recipe)