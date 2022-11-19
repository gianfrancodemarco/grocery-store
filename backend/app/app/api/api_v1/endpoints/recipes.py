from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Recipe])
def read_recipes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve recipes.
    """
    return crud.recipe.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Recipe)
def read_Recipe(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve Recipe.
    """
    return crud.recipe.get(db=db, id=id)

@router.post("/", response_model=schemas.Recipe)
def create_Recipe(
    *,
    db: Session = Depends(deps.get_db),
    Recipe_in: schemas.RecipeCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    Recipe = crud.recipe.create(db=db, obj_in=Recipe_in)
    return Recipe


@router.put("/{id}", response_model=schemas.Recipe)
def update_Recipe(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    Recipe_in: schemas.RecipeUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a Recipe.
    """
    Recipe = crud.recipe.get(db=db, id=id)
    if not Recipe:
        raise HTTPException(status_code=404, detail="Item not found")
    Recipe = crud.recipe.update(db=db, db_obj=Recipe, obj_in=Recipe_in)
    return Recipe


# @router.delete("/{id}", response_model=schemas.Item)
# def delete_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.remove(db=db, id=id)
#     return item
