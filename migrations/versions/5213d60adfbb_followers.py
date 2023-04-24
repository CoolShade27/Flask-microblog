"""followers

Revision ID: 5213d60adfbb
Revises: 0863a168f8b2
Create Date: 2023-04-24 19:31:00.725565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5213d60adfbb'
down_revision = '0863a168f8b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
