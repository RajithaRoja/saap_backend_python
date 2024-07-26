"""create_invalid_token

Revision ID: 39434b1c7920
Revises: 795235d90943
Create Date: 2024-06-03 14:52:42.716465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39434b1c7920'
down_revision: Union[str, None] = '795235d90943'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
      op.create_table(
        'logout_token',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('user_id',sa.Integer,nullable=False),
        sa.Column('token',sa.TEXT(),nullable=False,),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('deleted', sa.SmallInteger(), nullable=False, server_default="0"),
        sa.Column('record_status', sa.SmallInteger(), nullable=False, server_default="1"),
        sa.Column('created_by_id', sa.Integer(), nullable=False),
        sa.Column('updated_by_id', sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('logout_token')

