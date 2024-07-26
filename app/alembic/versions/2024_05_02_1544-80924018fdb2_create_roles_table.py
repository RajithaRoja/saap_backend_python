"""Create roles table

Revision ID: 80924018fdb2
Revises: f89ae916003a
Create Date: 2024-05-02 15:44:16.476531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80924018fdb2'
down_revision: Union[str, None] = 'f89ae916003a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'roles',
        sa.Column('id',sa.Integer, nullable=False, unique=True, autoincrement=True, primary_key=True),
        sa.Column('name',  sa.String(255), nullable=False, unique=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column('deleted', sa.SmallInteger, nullable=False, server_default=sa.text("0")),
        sa.Column('record_status', sa.SmallInteger, nullable=False, server_default=sa.text("1")),
        sa.Column('created_by_id', sa.Integer, nullable=False),
        sa.Column('updated_by_id', sa.Integer),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('roles')
