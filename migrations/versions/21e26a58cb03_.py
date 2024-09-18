"""empty message

Revision ID: 21e26a58cb03
Revises: e06cd70704be
Create Date: 2024-08-27 15:27:30.914201

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '21e26a58cb03'
down_revision = 'e06cd70704be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False, comment='送信者id'))
        batch_op.drop_column('sender_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sender_id', mysql.INTEGER(), autoincrement=False, nullable=False, comment='送信者id'))
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
