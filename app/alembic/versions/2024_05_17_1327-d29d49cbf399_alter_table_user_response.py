"""alter_table_user_response

Revision ID: d29d49cbf399
Revises: c48b56daee3d
Create Date: 2024-05-17 13:27:01.011226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd29d49cbf399'
down_revision: Union[str, None] = 'c48b56daee3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user_response', sa.Column('ai_response', sa.JSON, nullable=True))


def downgrade() -> None:
    op.drop_column('user_response', 'ai_response')