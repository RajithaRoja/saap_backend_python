"""Create subject table

Revision ID: 1b22f29092f9
Revises: 3cf80cb59592
Create Date: 2024-05-02 15:33:14.528094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b22f29092f9'
down_revision: Union[str, None] = '3cf80cb59592'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'subject',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('subject_name', sa.String(255), nullable=False),
        sa.Column('subject_code', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('deleted', sa.SmallInteger, nullable=False, server_default=sa.text("0")),
        sa.Column('record_status', sa.SmallInteger, nullable=False, server_default=sa.text("1")),
        sa.Column('created_by_id', sa.Integer, nullable=False),
        sa.Column('updated_by_id', sa.Integer),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('subject')
