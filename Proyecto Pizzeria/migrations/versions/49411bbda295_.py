"""empty message

Revision ID: 49411bbda295
Revises: bd330ba94581
Create Date: 2023-11-30 23:36:28.138698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49411bbda295'
down_revision = 'bd330ba94581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ingredientes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url_imagen', sa.String(length=1000), nullable=True))

    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url_imagen', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.drop_column('url_imagen')

    with op.batch_alter_table('ingredientes', schema=None) as batch_op:
        batch_op.drop_column('url_imagen')

    # ### end Alembic commands ###