"""Update Users

Revision ID: 5aa57e606b4b
Revises: a6630eb8a3c1
Create Date: 2023-03-19 14:05:27.161448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aa57e606b4b'
down_revision = 'a6630eb8a3c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('emp_city', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'emp_city')
    # ### end Alembic commands ###
