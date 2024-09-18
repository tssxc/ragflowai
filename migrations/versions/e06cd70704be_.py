"""empty message

Revision ID: e06cd70704be
Revises: af386407ddec
Create Date: 2024-08-27 13:31:29.371007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e06cd70704be'
down_revision = 'af386407ddec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.TIMESTAMP(), nullable=True, comment='创建时间'))
        batch_op.drop_column('timetamp')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timetamp', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='创建时间'))
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###
