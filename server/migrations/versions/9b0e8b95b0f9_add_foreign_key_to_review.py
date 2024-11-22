"""add foreign key to Review

Revision ID: 9b0e8b95b0f9
Revises: 72d910381f1e
Create Date: 2024-11-21 19:40:49.998924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b0e8b95b0f9'
down_revision = '72d910381f1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###