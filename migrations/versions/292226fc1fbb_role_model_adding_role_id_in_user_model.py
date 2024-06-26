"""Role model & adding role_id in User model

Revision ID: 292226fc1fbb
Revises: 3c8ef66868bb
Create Date: 2024-06-09 08:13:31.315830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '292226fc1fbb'
down_revision = '3c8ef66868bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'role', ['role_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('role_id')

    # ### end Alembic commands ###
