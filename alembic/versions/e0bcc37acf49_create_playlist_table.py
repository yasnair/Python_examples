"""create playlist table

Revision ID: e0bcc37acf49
Revises: 1f1ef86bb67e
Create Date: 2022-01-25 10:13:42.108640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0bcc37acf49'
down_revision = '1f1ef86bb67e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'playlist',
        sa.Column('id', sa.INTEGER, primary_key=True),
        sa.Column('playlist_id', sa.String(100), nullable=False), 
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),

    )


def downgrade():
    op.drop_table('playlist')
