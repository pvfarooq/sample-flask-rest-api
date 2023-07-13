"""create product table

Revision ID: 258d884c6a06
Revises: b208e46fef33
Create Date: 2023-07-11 21:27:02.791907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "258d884c6a06"
down_revision = "b208e46fef33"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "product",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("title", sa.String(255), nullable=False, unique=True),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["product_category.id"],
            name="fk_product_category_id",
        ),
    )


def downgrade() -> None:
    op.drop_table("product")
