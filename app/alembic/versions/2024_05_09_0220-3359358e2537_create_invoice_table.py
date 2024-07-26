"""create_invoice_table

Revision ID: 3359358e2537
Revises: b88c8b1e0d25
Create Date: 2024-05-09 02:20:08.975607

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3359358e2537'
down_revision: Union[str, None] = 'b88c8b1e0d25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'invoice',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('payment_id', sa.String(255), nullable=False),
        sa.Column('payment_date', sa.Date(), nullable=False),
        sa.Column('status', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('deleted', sa.SmallInteger(), nullable=False, server_default="0"),
        sa.Column('record_status', sa.SmallInteger(), nullable=False, server_default="1"),
        sa.Column('created_by_id', sa.Integer(), nullable=False),
        sa.Column('updated_by_id', sa.Integer(), nullable=True),
        sa.Column('stripe_invoice_id', sa.String(length=255), nullable=False),
        sa.Column('invoice_detail', sa.JSON(), nullable=True),
        sa.Column('next_invoice_date', sa.Date(), nullable=True),
        sa.Column('invoice_status', sa.String(length=255), nullable=True),
        sa.Column('file_path', sa.String(length=500), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('invoice')
