"""alter_drop_table_user_response

Revision ID: e2fb873201ec
Revises: 56224dd3a972
Create Date: 2024-05-13 00:03:57.439502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2fb873201ec'
down_revision: Union[str, None] = '56224dd3a972'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('question_ibfk_5', 'question', type_='foreignkey')
    op.drop_column('question', 'introtext_id')    
    op.add_column('question', sa.Column('introtext', sa.Text(), nullable=True))


def downgrade():
    op.add_column('question', sa.Column('introtext_id', sa.Integer(), nullable=True))

    op.create_foreign_key(
        'question_ibfk_5',
        'question',
        'introtext',
        ['introtext_id'],
        ['id']
    )
    op.drop_column('question', 'introtext')
