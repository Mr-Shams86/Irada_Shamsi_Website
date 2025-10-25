"""create portfolio_likes table

Revision ID: 3bb3623147d3
Revises: dac3e4607d2a
Create Date: 2025-10-24 19:54:36.377739

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision: str = "3bb3623147d3"
down_revision: Union[str, None] = "dac3e4607d2a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'portfolio_likes',
        sa.Column('id', sa.String(length=64), primary_key=True, nullable=False),
        sa.Column('count', sa.Integer(), nullable=False, server_default='0'),
        sa.CheckConstraint('count >= 0', name='ck_portfolio_likes_count_nonneg'),
    )
    op.create_index('ix_portfolio_likes_id', 'portfolio_likes', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_portfolio_likes_id', table_name='portfolio_likes')
    op.drop_table('portfolio_likes')
