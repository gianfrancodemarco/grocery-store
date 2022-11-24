from datetime import datetime
from typing import Optional

from app.enums.fruit_size_enum import FruitSizeEnum
from pydantic import BaseModel


# Shared properties
class TriggerAuditingBase(BaseModel):
    id: Optional[int] = None
    trigger_name: Optional[str] = None
    description: Optional[str] = None
    timestamp: Optional[datetime] = None


# Properties to receive on fruit creation
class TriggerAuditingCreate(TriggerAuditingBase):
    trigger_name: str = None

# Properties to receive on fruit update
class TriggerAuditingUpdate(TriggerAuditingBase):
    id: int = None

# Properties shared by models stored in DB
class TriggerAuditingInDBBase(TriggerAuditingBase):
    id: int = None
    trigger_name: str = None
    description: str = None
    timestamp: datetime = None

    class Config:
        orm_mode = True


# Properties to return to client
class TriggerAuditing(TriggerAuditingInDBBase):
    pass


# Properties properties stored in DB
class TriggerAuditingInDB(TriggerAuditingInDBBase):
    pass