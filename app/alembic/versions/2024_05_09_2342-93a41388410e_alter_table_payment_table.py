"""alter_table_payment_table

Revision ID: 93a41388410e
Revises: 4f1ba68b29a7
Create Date: 2024-05-09 23:42:30.673126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93a41388410e'
down_revision: Union[str, None] = '4f1ba68b29a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("UPDATE payment_history SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL")
    op.execute("UPDATE  user_roles SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL")
    op.execute("UPDATE  question_type SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL")

    op.alter_column('payment_history', 'created_at', existing_type=sa.TIMESTAMP(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP"))
    op.alter_column('user_roles', 'created_at', existing_type=sa.TIMESTAMP(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP"))
    op.alter_column('question_type', 'created_at', existing_type=sa.TIMESTAMP(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP"))


    op.alter_column('payment_history', 'updated_at', existing_type=sa.TIMESTAMP(), nullable=True, server_default=sa.text("CURRENT_TIMESTAMP"))
    op.alter_column('user_roles', 'updated_at', existing_type=sa.TIMESTAMP(), nullable=True, server_default=sa.text("CURRENT_TIMESTAMP"))
    op.alter_column('question_type', 'updated_at', existing_type=sa.TIMESTAMP(), nullable=True, server_default=sa.text("CURRENT_TIMESTAMP"))




def downgrade():
    op.alter_column('payment_history', 'updated_at', existing_type=sa.TIMESTAMP(), nullable=False, server_default=None)
    op.alter_column('user_roles', 'updated_at', existing_type=sa.TIMESTAMP(), nullable=False, server_default=None)
    op.alter_column('question_type', 'updated_at', existing_type=sa.TIMESTAMP(), nullable=False, server_default=None)

    op.alter_column('payment_history', 'created_at', existing_type=sa.TIMESTAMP(), nullable=True, server_default=None)
    op.alter_column('user_roles', 'created_at', existing_type=sa.TIMESTAMP(), nullable=True, server_default=None)
    op.alter_column('question_type', 'created_at', existing_type=sa.TIMESTAMP(), nullable=True, server_default=None)
