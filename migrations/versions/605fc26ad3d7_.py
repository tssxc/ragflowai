"""empty message

Revision ID: 605fc26ad3d7
Revises: 
Create Date: 2024-08-23 18:56:37.000086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605fc26ad3d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('username', sa.String(length=64), nullable=True, comment='用户名'),
    sa.Column('password', sa.String(length=128), nullable=True, comment='密码，加密保存'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    # ### end Alembic commands ###
