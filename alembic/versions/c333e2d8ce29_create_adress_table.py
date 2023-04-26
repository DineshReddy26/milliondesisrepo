"""create adress table

Revision ID: c333e2d8ce29
Revises: ff5332beb093
Create Date: 2023-04-26 06:01:24.608292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c333e2d8ce29'
down_revision = 'ff5332beb093'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id',sa.Integer,nullable=False,primary_key=True),
                    sa.Column('address1',sa.String,nullable=False),
                    sa.Column('address2',sa.String,nullable=False),
                    sa.Column('city',sa.String,nullable=False),
                    sa.Column('state',sa.String,nullable=False),
                    sa.Column('country',sa.String,nullable=False),
                    sa.Column('postalcode',sa.String,nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('address')
