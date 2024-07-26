"""create_user

Revision ID: 3cf80cb59592
Revises: 1e23c319a6be
Create Date: 2024-05-01 10:51:59.091474

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = "3cf80cb59592"
down_revision: Union[str, None] = "1e23c319a6be"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("email", sa.String(100), nullable=False),
        sa.Column("picture_url", sa.String(255), nullable=True),
        sa.Column("authentication_type", sa.String(255), nullable=False),
        sa.Column("external_login_id", sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(), nullable=True, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.Column("created_by", sa.SmallInteger(), nullable=True),
        sa.Column("updated_by", sa.SmallInteger(), nullable=True),
        sa.Column("deleted", sa.SmallInteger(), nullable=False, server_default="0"),
        sa.Column("record_status", sa.SmallInteger(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("user")
