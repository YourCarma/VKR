"""empty message

Revision ID: 8cb031428a20
Revises: 1790995c9260
Create Date: 2024-03-27 18:16:05.977799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cb031428a20'
down_revision: Union[str, None] = '1790995c9260'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sources', sa.Column('politic_view', sa.String(), nullable=False))
    op.drop_column('sources', 'poliric_view')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sources', sa.Column('poliric_view', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('sources', 'politic_view')
    # ### end Alembic commands ###
