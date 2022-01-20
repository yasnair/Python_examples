from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column 
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func


class Albums(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    album_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), unique=False, nullable=False)
    release_date = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    tracks = relationship("Tracks",
                        secondary="album_tracks",
                        backref="albums")

    def __repr__(self):
        return "<Album %r>" % self.album_id
