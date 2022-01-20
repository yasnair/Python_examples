from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func

class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    playlist = relationship("Playlist", backref="user") # one-to-many collection

    def __repr__(self):
        return "<User %r>" % self.username