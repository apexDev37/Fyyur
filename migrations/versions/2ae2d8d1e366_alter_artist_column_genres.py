"""ALTER Artist COLUMN genres.

Revision ID: 2ae2d8d1e366
Revises: 560ac4493717
Create Date: 2022-06-04 13:07:09.047907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ae2d8d1e366'
down_revision = '560ac4493717'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genre', sa.ARRAY(sa.String(length=120)), nullable=True))
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'genre')
    # ### end Alembic commands ###
