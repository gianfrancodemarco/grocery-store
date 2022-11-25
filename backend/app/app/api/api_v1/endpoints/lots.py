from typing import Any, List

import sqlalchemy
from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.Lot])
def read_lots(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve lots.
    """
    return crud.lot.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Lot)
def read_lot(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve lot.
    """
    return crud.lot.get(db=db, id=id)

@router.post("/", response_model=schemas.Lot)
def create_lot(
    *,
    db: Session = Depends(deps.get_db),
    lot_in: schemas.LotCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    try:
        lot = crud.lot.create(db=db, obj_in=lot_in)
    except sqlalchemy.exc.DatabaseError as exc:
        raise HTTPException(status_code=400, detail=exc.args[0])

    return lot


@router.put("/{id}", response_model=schemas.Lot)
def update_lot(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    lot_in: schemas.LotUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a lot.
    """
    lot = crud.lot.get(db=db, id=id)
    if not lot:
        raise HTTPException(status_code=404, detail="Item not found")

    try:
        lot = crud.lot.update(db=db, db_obj=lot, obj_in=lot_in)
    except sqlalchemy.exc.DatabaseError as exc:
        raise HTTPException(status_code=400, detail=exc.args[0])

    return lot


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
