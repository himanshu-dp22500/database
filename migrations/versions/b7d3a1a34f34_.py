"""empty message

Revision ID: b7d3a1a34f34
Revises: 6d1c103f7349
Create Date: 2024-05-28 11:29:47.234899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7d3a1a34f34'
down_revision: Union[str, None] = '6d1c103f7349'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'new_test_field')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('new_test_field', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###