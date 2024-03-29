"""empty message

Revision ID: e79afaee3c18
Revises: 37e469e3177a
Create Date: 2023-03-09 19:59:16.007626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e79afaee3c18'
down_revision = '37e469e3177a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('example', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.drop_column('example')

    # ### end Alembic commands ###
