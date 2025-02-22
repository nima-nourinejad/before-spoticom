"""update

Revision ID: 17b2bb76af8f
Revises: eb3731af8704
Create Date: 2025-02-22 08:27:30.367587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17b2bb76af8f'
down_revision = 'eb3731af8704'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    op.drop_index('ix_users_username', table_name='users')
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
