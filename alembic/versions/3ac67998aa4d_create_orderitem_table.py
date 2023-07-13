"""create orderitem table

Revision ID: 3ac67998aa4d
Revises: 44b236bc7272
Create Date: 2023-07-11 22:17:50.913829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3ac67998aa4d"
down_revision = "44b236bc7272"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "order_items",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("order_id", sa.Integer, nullable=False),
        sa.Column("product_id", sa.Integer, nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_order_item_user_id"
        ),
        sa.ForeignKeyConstraint(
            ["order_id"], ["orders.id"], name="fk_order_item_order_id"
        ),
        sa.ForeignKeyConstraint(
            ["product_id"], ["product.id"], name="fk_order_item_product_id"
        ),
    )


def downgrade() -> None:
    op.drop_table("order_items")
