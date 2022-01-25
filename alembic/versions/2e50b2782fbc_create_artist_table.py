"""create artist table

Revision ID: 2e50b2782fbc
Revises: 9469d31c366e
Create Date: 2022-01-25 10:12:22.127430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e50b2782fbc'
down_revision = '9469d31c366e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'artist',
        sa.Column('id', sa.INTEGER, primary_key=True),
        sa.Column('artist_id', sa.String(100), nullable=False), 
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )

def downgrade():
    op.drop_table('artist')
