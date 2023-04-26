"""create phone number for user col

Revision ID: ff5332beb093
Revises: 
Create Date: 2023-04-26 05:42:58.719703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff5332beb093'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone number', sa.String(),nullable=True))

def downgrade() -> None:
    op.drop_column('users','phone number')