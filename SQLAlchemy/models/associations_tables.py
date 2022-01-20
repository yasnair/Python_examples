from sqlalchemy import Column, ForeignKey, Table
from base import Base

playlists_tracks = Table('playlists_tracks', Base.metadata,
    Column('playlist_id', ForeignKey('playlist.id'), primary_key=True),
    Column('track_id', ForeignKey('track.id'), primary_key=True)
)

albums_tracks = Table('albums_tracks', Base.metadata,
    Column('album_id', ForeignKey('album.id'), primary_key=True),
    Column('track_id', ForeignKey('track.id'), primary_key=True)
)

artists_tracks = Table('artists_tracks', Base.metadata,
    Column('artist_id', ForeignKey('artist.id'), primary_key=True),
    Column('track_id', ForeignKey('track.id'), primary_key=True)
)