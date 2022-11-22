from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Sensor])
def read_sensors(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve sensors.
    """
    return crud.sensor.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Sensor)
def read_sensor(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve sensor.
    """
    return crud.sensor.get(db=db, id=id)

@router.post("/", response_model=schemas.Sensor)
def create_sensor(
    *,
    db: Session = Depends(deps.get_db),
    sensor_in: schemas.SensorCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    sensor = crud.sensor.create(db=db, obj_in=sensor_in)
    return sensor


@router.put("/{id}", response_model=schemas.Sensor)
def update_sensor(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    sensor_in: schemas.SensorUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a sensor.
    """
    sensor = crud.sensor.get(db=db, id=id)
    if not sensor:
        raise HTTPException(status_code=404, detail="Item not found")
    sensor = crud.sensor.update(db=db, db_obj=sensor, obj_in=sensor_in)
    return sensor


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
