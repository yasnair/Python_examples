"""create track table

Revision ID: 3f13137eb801
Revises: e0bcc37acf49
Create Date: 2022-01-25 10:13:58.855561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f13137eb801'
down_revision = 'e0bcc37acf49'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'track',
        sa.Column('id', sa.INTEGER, primary_key=True),
        sa.Column('track_id', sa.String(100), nullable=False), 
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('duration_ms', sa.INTEGER),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('track')
