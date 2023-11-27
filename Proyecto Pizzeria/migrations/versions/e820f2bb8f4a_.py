"""empty message

Revision ID: e820f2bb8f4a
Revises: a75dd07a0568
Create Date: 2023-11-24 01:50:09.935087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e820f2bb8f4a'
down_revision = 'a75dd07a0568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=False))
        batch_op.drop_column('contraseña')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contraseña', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###