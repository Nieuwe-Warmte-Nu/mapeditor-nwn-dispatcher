"""add esdl feedback messages

Revision ID: 8c22ec9e5d18
Revises: e037fa7ad61e
Create Date: 2024-11-28 15:31:29.358039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c22ec9e5d18'
down_revision: Union[str, None] = 'e037fa7ad61e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_rest', sa.Column('esdl_feedback', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job_rest', 'esdl_feedback')
    # ### end Alembic commands ###
