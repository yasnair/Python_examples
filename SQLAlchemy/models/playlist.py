
from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func


class Playlists(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    playlist_id = Column(String(100), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))  # Foreign key added
    name = Column(String(255), unique=False, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user  = relationship("User", backref="playlist") # many-to-one scalar
    tracks = relationship("Tracks",
                        secondary="playlist_tracks",
                        backref="playlists")

    def __repr__(self):
        return "<Playlist %r>" % self.playlist_id