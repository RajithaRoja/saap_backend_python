"""Create question table

Revision ID: 0374f729d87d
Revises: c37a06f15a06
Create Date: 2024-05-02 15:41:24.924097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0374f729d87d'
down_revision: Union[str, None] = 'c37a06f15a06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'question',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('parent_id', sa.Integer(),sa.ForeignKey('question.id'), nullable=True),
        sa.Column('paper_id', sa.Integer(), sa.ForeignKey('question_paper.id'), nullable=False,),
        sa.Column('question_text', sa.Text(), nullable=True),
        sa.Column('question_type', sa.Enum('MultipleChoice', 'Essay', 'Paragraph', 'Image', name='question_types'), nullable=False),
        sa.Column('question_rule', sa.Text(), nullable=True),
        sa.Column('mark', sa.Float(), nullable = False),
        sa.Column('question_number', sa.Integer(), nullable=False),
        sa.Column('subquestion_label',sa.String(255) , nullable=True),
        sa.Column('order', sa.Integer(), nullable=True),
        sa.Column('subject_id', sa.Integer(), sa.ForeignKey('subject.id'), nullable=False),
        sa.Column('section_id', sa.Integer(),  sa.ForeignKey('section.id'),nullable=False),
        sa.Column('introtext_id', sa.Integer(), sa.ForeignKey('introtext.id'), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('deleted', sa.SmallInteger, nullable=False, server_default=sa.text("0")),
        sa.Column('record_status', sa.SmallInteger, nullable=False, server_default=sa.text("1")),
        sa.Column('created_by_id', sa.Integer, nullable=False),
        sa.Column('updated_by_id', sa.Integer),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('question')