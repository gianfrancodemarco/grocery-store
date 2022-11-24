from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.db.custom_types import utcnow
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.oracle import TIMESTAMP
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
    last_read_notifications = Column(TIMESTAMP, server_default=utcnow())
