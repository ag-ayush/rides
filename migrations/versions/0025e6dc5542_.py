"""empty message

Revision ID: 0025e6dc5542
Revises: 
Create Date: 2020-05-03 01:20:32.431176

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0025e6dc5542'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('picture', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('token', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('owner', sa.String(length=50), nullable=False),
    sa.Column('sharing', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('creator', sa.String(length=50), nullable=False),
    sa.Column('expired', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userteam',
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('team_id', 'user_id')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('current_capacity', sa.Integer(), nullable=False),
    sa.Column('max_capacity', sa.Integer(), nullable=False),
    sa.Column('departure_time', sa.DateTime(), nullable=False),
    sa.Column('return_time', sa.DateTime(), nullable=False),
    sa.Column('driver_comment', sa.Text(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('passengers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('passengers')
    op.drop_table('cars')
    op.drop_table('userteam')
    op.drop_table('events')
    op.drop_table('team')
    op.drop_table('user')
    # ### end Alembic commands ###