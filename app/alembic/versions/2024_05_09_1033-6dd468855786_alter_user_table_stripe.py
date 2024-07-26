"""alter_user_table_stripe

Revision ID: 6dd468855786
Revises: 3359358e2537
Create Date: 2024-05-09 10:33:56.181825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6dd468855786'
down_revision: Union[str, None] = '3359358e2537'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('user', sa.Column('stripe_id', sa.String(length=255), nullable=True))


def downgrade():
    op.drop_column('user', 'stripe_id')