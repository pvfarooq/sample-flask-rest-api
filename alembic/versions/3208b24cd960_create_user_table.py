"""create user table

Revision ID: 3208b24cd960
Revises: 
Create Date: 2023-07-11 21:11:51.976923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3208b24cd960"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("username", sa.String(255), nullable=False, unique=True),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column("is_admin", sa.Boolean, default=True),
    )


def downgrade() -> None:
    op.drop_table("users")
