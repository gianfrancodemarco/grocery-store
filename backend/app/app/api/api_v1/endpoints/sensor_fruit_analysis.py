from typing import Any, List

import sqlalchemy
from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.SensorFruitAnalysis])
def read_sensor_fruit_analysiss(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve sensor_fruit_analysis_fruit_analysis.
    """
    return crud.sensor_fruit_analysis.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.SensorFruitAnalysis)
def read_sensor_fruit_analysis(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve sensor_fruit_analysis.
    """
    return crud.sensor_fruit_analysis.get(db=db, id=id)

@router.post("/", response_model=schemas.SensorFruitAnalysis)
def create_sensor_fruit_analysis(
    *,
    db: Session = Depends(deps.get_db),
    sensor_fruit_analysis_in: schemas.SensorFruitAnalysisCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    try:
        sensor_fruit_analysis = crud.sensor_fruit_analysis.create(db=db, obj_in=sensor_fruit_analysis_in)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail="Integrity error. An analysis already exist with those sensor_id and lot_id")
    except sqlalchemy.exc.DatabaseError as exc:
        raise HTTPException(status_code=400, detail=exc.args[0])

    return sensor_fruit_analysis


@router.put("/{id}", response_model=schemas.SensorFruitAnalysis)
def update_sensor_fruit_analysis(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    sensor_fruit_analysis_in: schemas.SensorFruitAnalysisUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a sensor_fruit_analysis.
    """
    sensor_fruit_analysis = crud.sensor_fruit_analysis.get(db=db, id=id)
    if not sensor_fruit_analysis:
        raise HTTPException(status_code=404, detail="Item not found")
    
    try:
        sensor_fruit_analysis = crud.sensor_fruit_analysis.update(db=db, db_obj=sensor_fruit_analysis, obj_in=sensor_fruit_analysis_in)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail="Integrity error. An analysis already exist with those sensor_id and lot_id")

    return sensor_fruit_analysis


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
