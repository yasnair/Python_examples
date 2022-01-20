from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column 
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func

class Artists(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    artist_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), unique=False, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    tracks = relationship("Tracks",
                        secondary="artists_tracks",
                        backref="artists")
    def __repr__(self):
        return "<Artist %r>" % self.artist_id
