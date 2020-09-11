"""empty message

Revision ID: d591778088d3
Revises: 992b043f46f0
Create Date: 2020-09-11 03:17:06.059875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd591778088d3'
down_revision = '992b043f46f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puzzle', sa.Column('age_range', sa.String(length=10), nullable=False))
    op.add_column('puzzle', sa.Column('category', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puzzle', 'category')
    op.drop_column('puzzle', 'age_range')
    # ### end Alembic commands ###
