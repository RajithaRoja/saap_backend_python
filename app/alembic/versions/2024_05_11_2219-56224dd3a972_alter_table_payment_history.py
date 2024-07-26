"""alter_table_payment_history

Revision ID: 56224dd3a972
Revises: effeff294db4
Create Date: 2024-05-11 22:19:28.744543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56224dd3a972'
down_revision: Union[str, None] = 'effeff294db4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('payment_history', 'stripe_subscription_id')

def downgrade() -> None:
    op.add_column('payment_history', sa.Column('stripe_subscription_id', sa.Integer, nullable=False))
