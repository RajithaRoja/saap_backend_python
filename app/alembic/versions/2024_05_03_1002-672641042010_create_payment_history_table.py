"""Create payment_history table

Revision ID: 672641042010
Revises: e894ef0ed354
Create Date: 2024-05-03 10:02:26.275835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '672641042010'
down_revision: Union[str, None] = 'e894ef0ed354'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table('payment_history',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('payment_date', sa.Date(), nullable=False),
        sa.Column('total_amount', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('deleted', sa.SmallInteger(), server_default="0", nullable=False),
        sa.Column('record_status', sa.SmallInteger(), server_default="1", nullable=False),
        sa.Column('created_by_id', sa.Integer(), nullable=False),
        sa.Column('updated_by_id', sa.Integer(), nullable=True),
        sa.Column('stripe_payment_intent_id', sa.String(length=255), nullable=True),
        sa.Column('stripe_checkout_id', sa.String(length=255), nullable=False),
        sa.Column('customer_id', sa.String(length=255), nullable=True),
        sa.Column('stripe_transaction_status', sa.String(length=255), nullable=False),
        sa.Column('cancelled_date', sa.Date(), nullable=True),
        sa.Column('cancellation_type', sa.Integer(), nullable=True),
        sa.Column('next_payment_date', sa.Date(), nullable=True),
        sa.Column('payment_intent_detail', sa.JSON(), nullable=True),
        sa.Column('checkout_detail', sa.JSON(), nullable=True),
        sa.Column('invoice_detail', sa.JSON(), nullable=True),
        sa.Column('stripe_subscription_id', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('payment_history')