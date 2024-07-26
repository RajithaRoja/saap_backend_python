"""update_question_table

Revision ID: 795235d90943
Revises: d29d49cbf399
Create Date: 2024-05-23 10:49:46.089487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '795235d90943'
down_revision: Union[str, None] = 'd29d49cbf399'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.add_column('question', sa.Column('prompt_text', sa.Text, nullable=True))


def downgrade() -> None:
    op.drop_column('question','prompt_text')
