
from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column 
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func


class Tracks(Base):
    __tablename__ = "track"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    track_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), unique=False, nullable=False)
    duration_ms = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    def __repr__(self):
        return "<Track_id %r>" % self.track_id
