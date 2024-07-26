"""alter_question_paper_table

Revision ID: b88c8b1e0d25
Revises: 5c4a451e95a4
Create Date: 2024-05-08 14:57:23.334812

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b88c8b1e0d25"
down_revision: Union[str, None] = "5c4a451e95a4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("question_paper", "month")
    op.add_column(
        "question_paper",
        sa.Column("assessment_specification", sa.String(255), nullable=False),
    )
    op.add_column("question_paper", sa.Column("topic_name", sa.Text(), nullable=False))
    op.drop_column("question_paper", "description")
    op.drop_column("question_paper", "title")


def downgrade() -> None:
    op.add_column("question_paper", sa.Column("title", sa.String(255), nullable=False))
    op.add_column("question_paper", sa.Column("description", sa.Text(), nullable=False))
    op.drop_column("question_paper", "assessment_specification")
    op.drop_column("question_paper", "topic_name")
    op.add_column(
        "question_paper",
        sa.Column(
            "month",
            sa.Enum(
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ),
            nullable=False,
        ),
    )
