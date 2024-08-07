"""Updated Task model

Revision ID: 8144cb4b9eff
Revises: 68572e996467
Create Date: 2024-06-21 00:50:09.271266

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8144cb4b9eff'
down_revision = '68572e996467'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contactNumber', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('status', sa.Boolean(), nullable=True))
        batch_op.alter_column('entityname',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('date',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.alter_column('time',
               existing_type=postgresql.TIME(),
               nullable=False)
        batch_op.alter_column('taskType',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('contactperson',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('contactperson',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('taskType',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('time',
               existing_type=postgresql.TIME(),
               nullable=True)
        batch_op.alter_column('date',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.alter_column('entityname',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('status')
        batch_op.drop_column('contactNumber')

    # ### end Alembic commands ###
