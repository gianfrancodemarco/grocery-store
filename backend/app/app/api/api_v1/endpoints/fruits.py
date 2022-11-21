from typing import Any, List

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.Fruit])
def read_fruits(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve fruits.
    """
    return crud.fruit.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Fruit)
def read_fruit(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve fruit.
    """
    return crud.fruit.get(db=db, id=id)

@router.post("/", response_model=schemas.Fruit)
def create_fruit(
    *,
    db: Session = Depends(deps.get_db),
    fruit_in: schemas.FruitCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    fruit = crud.fruit.create(db=db, obj_in=fruit_in)
    return fruit


@router.put("/{id}", response_model=schemas.Fruit)
def update_fruit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    fruit_in: schemas.FruitUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a fruit.
    """
    fruit = crud.fruit.get(db=db, id=id)
    if not fruit:
        raise HTTPException(status_code=404, detail="Item not found")
    fruit = crud.fruit.update(db=db, db_obj=fruit, obj_in=fruit_in)
    return fruit


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
