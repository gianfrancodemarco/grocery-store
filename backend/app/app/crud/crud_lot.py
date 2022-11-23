from typing import Any, Dict, Optional, Union

from app.crud.base import CRUDBase
from app.models.lot import Lot
from app.schemas.lot import LotCreate, LotUpdate
from sqlalchemy.orm import Session


class CRUDLot(CRUDBase[Lot, LotCreate, LotUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Lot]:
        return db.query(Lot).filter(Lot.name == name).first()

    def create(self, db: Session, *, obj_in: LotCreate) -> Lot:
        db_obj = Lot(
            name=obj_in.name,
            fruit_id=obj_in.fruit_id,
            timestamp_arrival=obj_in.timestamp_arrival,
            weight=obj_in.weight,
            volume=obj_in.volume,
            ripens_level=obj_in.ripens_level
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Lot, obj_in: Union[LotUpdate, Dict[str, Any]]
    ) -> Lot:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

lot = CRUDLot(Lot)
