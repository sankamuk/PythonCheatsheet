"""Initial Setup

Revision ID: a6630eb8a3c1
Revises: 
Create Date: 2023-03-19 13:50:00.610801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6630eb8a3c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('emp_id', sa.Integer(), nullable=False),
    sa.Column('emp_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('emp_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###