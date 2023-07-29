"""Rename table user -> users

Revision ID: fa4da53716da
Revises: e6cbef14228f
Create Date: 2023-07-29 13:21:39.293059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa4da53716da'
down_revision = 'e6cbef14228f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    op.drop_constraint('booking_user_id_fkey', 'booking', type_='foreignkey')
    op.create_foreign_key(None, 'booking', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'booking', type_='foreignkey')
    op.create_foreign_key('booking_user_id_fkey', 'booking', 'user', ['user_id'], ['id'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('users')
    # ### end Alembic commands ###