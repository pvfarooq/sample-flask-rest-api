"""create order table

Revision ID: 44b236bc7272
Revises: 258d884c6a06
Create Date: 2023-07-11 21:30:04.073932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "44b236bc7272"
down_revision = "258d884c6a06"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("is_completed", sa.Boolean, default=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_orders_user_id"),
    )


def downgrade() -> None:
    op.drop_table("orders")
