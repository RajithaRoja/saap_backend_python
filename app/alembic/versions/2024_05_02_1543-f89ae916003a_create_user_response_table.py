"""Create user_response table

Revision ID: f89ae916003a
Revises: c46f1557cef2
Create Date: 2024-05-02 15:43:34.037485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f89ae916003a'
down_revision: Union[str, None] = 'c46f1557cef2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'user_responses',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('question_id', sa.Integer(), sa.ForeignKey('question.id'),nullable=False),
        sa.Column('question_paper_id', sa.Integer(),sa.ForeignKey('question_paper.id'), nullable=False),
        sa.Column('option_id', sa.Integer(), sa.ForeignKey('option.id'),nullable=True),
        sa.Column('answer_text', sa.String(255), nullable=True),
        sa.Column('ai_feedback', sa.String(255), nullable=True),
        sa.Column('ai_score', sa.Float(), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('deleted', sa.SmallInteger, nullable=False, server_default=sa.text("0")),
        sa.Column('record_status', sa.SmallInteger, nullable=False, server_default=sa.text("1")),
        sa.Column('created_by_id', sa.Integer, nullable=False),
        sa.Column('updated_by_id', sa.Integer),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('user_responses')
