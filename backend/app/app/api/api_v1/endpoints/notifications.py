from typing import Any, List

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.TriggerAuditing])
def read_trigger_auditings(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve trigger_auditings.
    """
    return crud.trigger_auditing.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.TriggerAuditing)
def read_trigger_auditing(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve trigger_auditing.
    """
    return crud.trigger_auditing.get(db=db, id=id)

@router.get("/unread/count", response_model=int)
def read_trigger_auditing_unread(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve trigger_auditing.
    """
    return crud.trigger_auditing.get_user_unread(db=db, user_id=current_user.id)

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
