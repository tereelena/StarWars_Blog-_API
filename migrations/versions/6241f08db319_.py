"""empty message

Revision ID: 6241f08db319
Revises: 00b737c780e3
Create Date: 2021-09-04 00:24:11.845763

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6241f08db319'
down_revision = '00b737c780e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person', 'gender',
               existing_type=mysql.VARCHAR(length=1),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person', 'gender',
               existing_type=mysql.VARCHAR(length=1),
               nullable=False)
    # ### end Alembic commands ###
