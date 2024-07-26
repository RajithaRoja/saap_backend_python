"""Create introtext table

Revision ID: c37a06f15a06
Revises: fc14fad33835
Create Date: 2024-05-02 15:37:06.955864

"""
from typing import Sequence, Union
from sqlalchemy import Enum
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c37a06f15a06'
down_revision: Union[str, None] = 'fc14fad33835'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'introtext',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('type', Enum('Text', 'image'), nullable = False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('deleted', sa.SmallInteger, nullable=False, server_default=sa.text("0")),
        sa.Column('record_status', sa.SmallInteger, nullable=False, server_default=sa.text("1")),
        sa.Column('created_by_id', sa.Integer, nullable=False),
        sa.Column('updated_by_id', sa.Integer),
        sa.PrimaryKeyConstraint('id'),
        )


def downgrade() -> None:
    op.drop_table('introtext')