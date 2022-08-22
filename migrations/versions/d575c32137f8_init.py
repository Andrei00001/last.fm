"""init

Revision ID: d575c32137f8
Revises: 
Create Date: 2022-08-22 16:06:13.006321

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = 'd575c32137f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('telegram_id', sa.Integer(), nullable=False),
    sa.Column('date_reg', sa.DateTime(), nullable=False),
    sa.Column('token_fm', sa.String(), nullable=False),
    sa.Column('last_auth', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###