"""empty message

Revision ID: 2de451f03b48
Revises: 5b1f4c9d0d43
Create Date: 2019-03-28 23:39:42.164409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2de451f03b48'
down_revision = '5b1f4c9d0d43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bucket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('owner', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bucketevent',
    sa.Column('bucket_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bucket_id'], ['bucket.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('bucket_id', 'event_id')
    )
    op.add_column('events', sa.Column('bucket_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'events', 'bucket', ['bucket_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'bucket_id')
    op.drop_table('bucketevent')
    op.drop_table('bucket')
    # ### end Alembic commands ###