from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from app.crud.base import CRUDBase
from app.crud.crud_user import user
from app.models.trigger_auditing import TriggerAuditing
from app.schemas.trigger_auditing import (TriggerAuditingCreate,
                                          TriggerAuditingUpdate)
from sqlalchemy.orm import Session


class CRUDTriggerAuditing(CRUDBase[TriggerAuditing, TriggerAuditingCreate, TriggerAuditingUpdate]):
    
    def get_user_unread(self, db: Session, user_id: int) -> Optional[TriggerAuditing]:
        current_user = db.query(user.model).filter(user.model.id == user_id).first()
        return db.query(self.model).filter(self.model.timestamp > current_user.last_read_notifications).count()


trigger_auditing = CRUDTriggerAuditing(TriggerAuditing)
