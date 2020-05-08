"""empty message

Revision ID: d50279c1f8aa
Revises: abf2a4a1ab6a
Create Date: 2020-05-07 16:38:00.224126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd50279c1f8aa'
down_revision = 'abf2a4a1ab6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('APIKey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hash', sa.String(length=64), nullable=True),
    sa.Column('owner', sa.String(length=80), nullable=True),
    sa.Column('reason', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash'),
    sa.UniqueConstraint('owner', 'reason', name='unique_key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('APIKey')
    # ### end Alembic commands ###
