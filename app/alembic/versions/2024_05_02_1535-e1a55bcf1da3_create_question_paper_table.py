"""Create question_paper table

Revision ID: e1a55bcf1da3
Revises: 1b22f29092f9
Create Date: 2024-05-02 15:35:38.685271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Enum


# revision identifiers, used by Alembic.
revision: str = 'e1a55bcf1da3'
down_revision: Union[str, None] = '1b22f29092f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.create_table(
        'question_paper',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),  
        sa.Column('year', sa.Integer, nullable=False),        
        sa.Column('month', Enum('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), nullable=False),
        sa.Column('subject_id', sa.Integer(), sa.ForeignKey('subject.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('deleted', sa.SmallInteger, nullable=False, server_default=sa.text("0")),
        sa.Column('record_status', sa.SmallInteger, nullable=False, server_default=sa.text("1")),
        sa.Column('created_by_id', sa.Integer, nullable=False),
        sa.Column('updated_by_id', sa.Integer),
        sa.PrimaryKeyConstraint('id'),
        )


def downgrade() -> None:
    op.drop_table('question_paper')