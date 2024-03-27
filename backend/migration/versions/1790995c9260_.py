"""empty message

Revision ID: 1790995c9260
Revises: 8a9479ab93ee
Create Date: 2024-03-27 18:15:46.094794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1790995c9260'
down_revision: Union[str, None] = '8a9479ab93ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sources', sa.Column('poliric_view', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sources', 'poliric_view')
    # ### end Alembic commands ###
