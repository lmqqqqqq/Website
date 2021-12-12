"""add confirmation token

Revision ID: af7bc067971d
Revises: 8484ec63af68
Create Date: 2021-12-12 15:46:35.774769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af7bc067971d'
down_revision = '8484ec63af68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed')
    # ### end Alembic commands ###
