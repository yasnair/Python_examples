"""create user table

Revision ID: 8e5876f044ca
Revises: 
Create Date: 2022-01-25 10:11:01.694444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e5876f044ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.INTEGER, primary_key=True),
        sa.Column('user_id', sa.String(100), nullable=False), 
        sa.Column('display_name', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )

def downgrade():
    op.drop_table('user')
