"""alter_updated_at_column

Revision ID: effeff294db4
Revises: 93a41388410e
Create Date: 2024-05-10 00:01:17.816856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'effeff294db4'
down_revision: Union[str, None] = '93a41388410e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('option', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('subject', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('question_paper', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('section', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('introtext', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('question', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('paper_score', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('user_responses', 'updated_at', existing_type=sa.DateTime, nullable=True)
    op.alter_column('endpoint', 'updated_at', existing_type=sa.DateTime, nullable=True)


def downgrade() -> None:
    op.alter_column('option', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('subject', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('question_paper', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('section', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('introtext', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('question', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('paper_score', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('user_responses', 'updated_at', existing_type=sa.DateTime, nullable=False)
    op.alter_column('endpoint', 'updated_at', existing_type=sa.DateTime, nullable=False)
