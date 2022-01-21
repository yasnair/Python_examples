# 1 - imports
from base import Session, engine, Base
from album import Albums
from artist import Artists
from playlist import Playlists
from track import Tracks
from user import Users
from associations_tables import playlists_tracks, albums_tracks, artists_tracks


# 2 - generate database schema
Base.metadata.create_all(engine)



