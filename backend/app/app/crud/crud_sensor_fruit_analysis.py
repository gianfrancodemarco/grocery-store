from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.sensor_fruit_analysis import SensorFruitAnalysis
from app.schemas.sensor_fruit_analysis import SensorFruitAnalysisCreate, SensorFruitAnalysisUpdate
from sqlalchemy.orm import Session


class CRUDSensorFruitAnalysis(CRUDBase[SensorFruitAnalysis, SensorFruitAnalysisCreate, SensorFruitAnalysisUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[SensorFruitAnalysis]:
        return db.query(SensorFruitAnalysis).filter(SensorFruitAnalysis.name == name).first()

    def create(self, db: Session, *, obj_in: SensorFruitAnalysisCreate) -> SensorFruitAnalysis:
        db_obj = SensorFruitAnalysis(
            description=obj_in.description,
            sensor_id=obj_in.sensor_id,
            lot_id=obj_in.lot_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: SensorFruitAnalysis, obj_in: Union[SensorFruitAnalysisUpdate, Dict[str, Any]]
    ) -> SensorFruitAnalysis:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

sensor_fruit_analysis = CRUDSensorFruitAnalysis(SensorFruitAnalysis)
