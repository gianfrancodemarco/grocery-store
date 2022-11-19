from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Allergy])
def read_allergies(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve allergies.
    """
    return crud.allergy.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Allergy)
def read_allergy(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve allergy.
    """
    return crud.allergy.get(db=db, id=id)

@router.post("/", response_model=schemas.Allergy)
def create_allergy(
    *,
    db: Session = Depends(deps.get_db),
    allergy_in: schemas.AllergyCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    allergy = crud.allergy.create(db=db, obj_in=allergy_in)
    return allergy


@router.put("/{id}", response_model=schemas.Allergy)
def update_allergy(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    allergy_in: schemas.AllergyUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a allergy.
    """
    allergy = crud.allergy.get(db=db, id=id)
    if not allergy:
        raise HTTPException(status_code=404, detail="Item not found")
    allergy = crud.allergy.update(db=db, db_obj=allergy, obj_in=allergy_in)
    return allergy


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
