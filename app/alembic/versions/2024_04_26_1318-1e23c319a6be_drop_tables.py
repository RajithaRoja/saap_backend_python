"""drop_tables

Revision ID: 1e23c319a6be
Revises: 07335381d7a6
Create Date: 2024-04-26 13:18:29.190254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e23c319a6be'
down_revision: Union[str, None] = '07335381d7a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('question_type')
    op.drop_table('options_table')
    op.drop_table('questions_table')
    op.drop_table('subject_years')
    op.drop_table('subject')
    op.drop_table('users')



def downgrade() -> None:
    pass
