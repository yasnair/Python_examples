from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, DateTime, Float
from sqlalchemy.sql import func
from database import engine


Base = declarative_base()

class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    playlist = relationship("Playlist", backref="user")

    def __repr__(self):
        return "<User %r>" % self.username

class Playlist(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    playlist_id = Column(String(100), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))  # Foreign key added
    track_id = Column(Integer, ForeignKey("track.id"))  # Foreign key added
    name = Column(String(255), unique=False, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user  = relationship("User", backref="playlist")
    track = relationship("Tracks")

    def __repr__(self):
        return "<Playlist %r>" % self.playlist_id


class Tracks(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    track_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), unique=False, nullable=False)
    duration_ms = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships

    def __repr__(self):
        return "<Playlist %r>" % self.playlist_id

class Albums(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    album_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), unique=False, nullable=False)
    release_date = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships

    def __repr__(self):
        return "<Playlist %r>" % self.playlist_id

class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    artist_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), unique=False, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships

    def __repr__(self):
        return "<Playlist %r>" % self.playlist_id

Base.metadata.create_all(engine)