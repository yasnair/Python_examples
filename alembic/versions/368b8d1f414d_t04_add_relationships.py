"""T04:Add relationships

Revision ID: 368b8d1f414d
Revises: 3f13137eb801
Create Date: 2022-01-25 19:33:35.632681

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import relationship


# revision identifiers, used by Alembic.
revision = '368b8d1f414d'
down_revision = '3f13137eb801'
branch_labels = None
depends_on = None


def upgrade():

    #New columns playlist table
    op.add_column('playlist', sa.Column('collaborative', sa.BOOLEAN))
    op.add_column('playlist', sa.Column('public', sa.BOOLEAN))
    op.add_column('playlist', sa.Column('description', sa.Unicode(200)))


    op.create_table(
        'user_playlist',
        sa.Column('id_user', sa.INTEGER, primary_key=True),
        sa.Column('id_playlist', sa.INTEGER, primary_key=True),
        sa.Column('is_owner', sa.BOOLEAN),
       # sa.ForeignKeyConstraint(('id_user', 'id_playlist'), ['user.id'], ['playlist.id'])
        sa.ForeignKeyConstraint(['id_user'],['user.id'],),
        sa.ForeignKeyConstraint(['id_playlist'],['playlist.id'],),
    )

    op.create_table(
        'playlists_tracks',
        sa.Column('id_playlist', sa.INTEGER, primary_key=True),
        sa.Column('id_track', sa.INTEGER, primary_key=True),
        #sa.ForeignKeyConstraint(('id_playlist', 'id_track'), ['playlist.id'], ['track.id'])
        sa.ForeignKeyConstraint(['id_playlist'],['playlist.id'],),
        sa.ForeignKeyConstraint(['id_track'],['track.id'],),
    )

    op.create_table(
        'albums_tracks',
        sa.Column('id_album', sa.INTEGER, primary_key=True),
        sa.Column('id_track', sa.INTEGER, primary_key=True),
        #sa.ForeignKeyConstraint(('id_album', 'id_track'), ['album.id'], ['track.id'])
        sa.ForeignKeyConstraint(['id_album'],['album.id'],),
        sa.ForeignKeyConstraint(['id_track'],['track.id'],),
    )
    op.create_table(
        'artists_tracks',
        sa.Column('id_artist', sa.INTEGER, primary_key=True),
        sa.Column('id_track', sa.INTEGER, primary_key=True),
       # sa.ForeignKeyConstraint(('id_artist', 'id_track'), ['artist.id'], ['track.id'])
        sa.ForeignKeyConstraint(['id_artist'],['artist.id'],),
        sa.ForeignKeyConstraint(['id_track'],['track.id'],),
    )

    op.create_table(
        'user_tracks',
        sa.Column('id_user', sa.INTEGER, primary_key=True),
        sa.Column('id_track', sa.INTEGER, primary_key=True),
        #a.ForeignKeyConstraint(('id_user', 'id_track'), ['user.id'], ['track.id'])
        sa.ForeignKeyConstraint(['id_user'],['user.id'],),
        sa.ForeignKeyConstraint(['id_track'],['track.id'],),
    )



def downgrade():
    op.drop_table('user_playlist')
    op.drop_table('playlists_tracks')
    op.drop_table('albums_tracks')
    op.drop_table('artists_tracks')
    op.drop_table('user_tracks')
    op.drop_column('playlist','collaborative')
    op.drop_column('playlist','public')
    op.drop_column('playlist','description')
