"""create album table

Revision ID: 9469d31c366e
Revises: 8e5876f044ca
Create Date: 2022-01-25 10:11:50.499599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9469d31c366e'
down_revision = '8e5876f044ca'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'album',
        sa.Column('id', sa.INTEGER, primary_key=True),
        sa.Column('album_id', sa.String(100), nullable=False), 
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('release_date', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),

    )

def downgrade():
    op.drop_table('album')
