"""empty message
Revision ID: 1a7b2fa4bad6
Revises: 9a09b0829283
Create Date: 2022-03-17 00:02:46.607911
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1a7b2fa4bad6'
down_revision = '9a09b0829283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('_password', sa.String(length=128), nullable=False))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.drop_column('user', '_password')
    # ### end Alembic commands ###