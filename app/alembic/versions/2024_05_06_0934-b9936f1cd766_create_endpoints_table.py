"""create_endpoints_table

Revision ID: b9936f1cd766
Revises: 672641042010
Create Date: 2024-05-06 09:34:47.824715

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b9936f1cd766"
down_revision: Union[str, None] = "672641042010"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "endpoint",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(length=255), nullable=True),
        sa.Column(
            "default_role_access_id",
            sa.Integer(),
            sa.ForeignKey("roles.id"),
            nullable=False,
        ),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column(
            "deleted", sa.SmallInteger, nullable=False, server_default=sa.text("0")
        ),
        sa.Column(
            "record_status",
            sa.SmallInteger,
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.Column("created_by_id", sa.Integer, nullable=False),
        sa.Column("updated_by_id", sa.Integer),
        sa.PrimaryKeyConstraint("id"),
    )
    op.execute(""" ALTER TABLE user ADD COLUMN role_id INT(11) """)


def downgrade():
    op.drop_table("endpoint")
    op.execute(""" ALTER TABLE user DROP COLUMN role_id """)
