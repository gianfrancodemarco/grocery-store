from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.db.custom_types import utcnow
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.oracle import TIMESTAMP

if TYPE_CHECKING:
    from .trigger_auditing import TriggerAuditing  # noqa: F401

class TriggerAuditing(Base):
    __tablename__: str = "TRIGGER_AUDITING"

    id = Column(Integer, primary_key=True, index=True)
    trigger_name = Column(String(100))
    description = Column(String(1000))
    timestamp = Column(TIMESTAMP, server_default=utcnow())
