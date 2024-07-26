"""alter_table_invoice

Revision ID: 4f1ba68b29a7
Revises: 6dd468855786
Create Date: 2024-05-09 23:34:26.143911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f1ba68b29a7'
down_revision: Union[str, None] = '6dd468855786'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Single column indexes
    op.create_index(op.f('idx_payment_id'), 'invoice', ['payment_id'])
    op.create_index(op.f('idx_status'), 'invoice', ['status'])
    op.create_index(op.f('idx_created_at'), 'invoice', ['created_at'])

    # Composite indexes
    op.create_index(op.f('idx_payment_id_payment_date'), 'invoice', ['payment_id', 'payment_date'])
    op.create_index(op.f('idx_created_by_id_created_at'), 'invoice', ['created_by_id', 'created_at'])

def downgrade():
    op.drop_index(op.f('idx_payment_id'), table_name='invoice')
    op.drop_index(op.f('idx_status'), table_name='invoice')
    op.drop_index(op.f('idx_created_at'), table_name='invoice')
    op.drop_index(op.f('idx_payment_id_payment_date'), table_name='invoice')
    op.drop_index(op.f('idx_created_by_id_created_at'), table_name='invoice')
