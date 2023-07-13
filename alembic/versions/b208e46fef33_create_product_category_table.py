"""create product category table

Revision ID: b208e46fef33
Revises: 3208b24cd960
Create Date: 2023-07-11 21:26:11.015155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b208e46fef33"
down_revision = "3208b24cd960"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "product_category",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("title", sa.String(255), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("product_category")
