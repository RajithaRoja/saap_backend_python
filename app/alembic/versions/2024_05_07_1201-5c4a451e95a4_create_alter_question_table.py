"""Create alter question table 

Revision ID: 5c4a451e95a4
Revises: be839c8ba873
Create Date: 2024-05-07 12:01:43.444826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c4a451e95a4'
down_revision: Union[str, None] = 'be839c8ba873'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('question', sa.Column('source_text', sa.String(255), nullable=True))
    op.drop_column('question', 'question_type')
    op.add_column('question', sa.Column('question_type_id', sa.Integer(),sa.ForeignKey('question_type.id'), nullable=False))



def downgrade():
    op.drop_column('question', 'question_type_id')
    op.add_column('question', sa.Column('question_type', sa.Enum('MultipleChoice', 'Essay', 'Paragraph', 'Image', name='question_types'), nullable=False))
    op.drop_column('question', 'source_text')
