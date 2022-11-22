from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.sensor import Sensor
from app.schemas.sensor import SensorCreate, SensorUpdate
from sqlalchemy.orm import Session


class CRUDSensor(CRUDBase[Sensor, SensorCreate, SensorUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Sensor]:
        return db.query(Sensor).filter(Sensor.name == name).first()

    def create(self, db: Session, *, obj_in: SensorCreate) -> Sensor:
        db_obj = Sensor(
            name=obj_in.name,
            fruit_size=obj_in.fruit_size,
            medium_energy_consumption=obj_in.medium_energy_consumption,
            cost=obj_in.cost,
            brand=obj_in.brand
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Sensor, obj_in: Union[SensorUpdate, Dict[str, Any]]
    ) -> Sensor:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

sensor = CRUDSensor(Sensor)
