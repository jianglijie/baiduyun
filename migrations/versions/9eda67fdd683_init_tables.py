"""init tables

Revision ID: 9eda67fdd683
Revises: 
Create Date: 2017-10-09 17:37:13.907724

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9eda67fdd683'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('share_file',
    sa.Column('fid', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('uk', sa.BigInteger(), nullable=True),
    sa.Column('short_url', sa.String(length=15), nullable=True),
    sa.Column('is_dir', mysql.TINYINT(), nullable=True),
    sa.Column('size', sa.BigInteger(), nullable=True),
    sa.Column('md5', sa.String(length=32), nullable=True),
    sa.Column('share_id', sa.String(length=20), nullable=True),
    sa.Column('deleted', mysql.TINYINT(), nullable=True),
    sa.Column('d_cnt', sa.INTEGER(), nullable=True),
    sa.Column('ext', sa.String(length=10), nullable=True),
    sa.Column('create_time', sa.INTEGER(), nullable=True),
    sa.Column('file_type', mysql.TINYINT(), nullable=True),
    sa.Column('uid', sa.BigInteger(), nullable=True),
    sa.Column('feed_type', sa.String(length=10), nullable=True),
    sa.Column('feed_time', sa.INTEGER(), nullable=True),
    sa.Column('indexed', mysql.TINYINT(), nullable=True),
    sa.PrimaryKeyConstraint('fid')
    )
    op.create_index(op.f('ix_share_file_feed_type'), 'share_file', ['feed_type'], unique=False)
    op.create_index(op.f('ix_share_file_file_type'), 'share_file', ['file_type'], unique=False)
    op.create_index(op.f('ix_share_file_indexed'), 'share_file', ['indexed'], unique=False)
    op.create_index(op.f('ix_share_file_is_dir'), 'share_file', ['is_dir'], unique=False)
    op.create_index(op.f('ix_share_file_uid'), 'share_file', ['uid'], unique=False)
    op.create_table('share_user',
    sa.Column('uid', sa.BigInteger(), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('uk', sa.BigInteger(), nullable=True),
    sa.Column('avatar_url', sa.String(length=200), nullable=True),
    sa.Column('intro', sa.TEXT(), nullable=True),
    sa.Column('follow_count', sa.INTEGER(), nullable=True),
    sa.Column('fans_count', sa.INTEGER(), nullable=True),
    sa.Column('pubshare_count', sa.INTEGER(), nullable=True),
    sa.Column('album_count', sa.INTEGER(), nullable=True),
    sa.Column('last_visited', sa.INTEGER(), nullable=True),
    sa.Column('weight', mssql.TINYINT(), nullable=True),
    sa.Column('create_time', sa.INTEGER(), nullable=True),
    sa.Column('visited_count', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('uk')
    )
    op.create_table('spider_list',
    sa.Column('sid', sa.BigInteger(), nullable=False),
    sa.Column('uk', sa.BigInteger(), nullable=True),
    sa.Column('file_fetched', sa.INTEGER(), nullable=True),
    sa.Column('follow_fetched', sa.INTEGER(), nullable=True),
    sa.Column('follow_done', mssql.TINYINT(), nullable=True),
    sa.Column('file_done', mssql.TINYINT(), nullable=True),
    sa.Column('weight', mssql.TINYINT(), nullable=True),
    sa.Column('uid', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('sid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spider_list')
    op.drop_table('share_user')
    op.drop_index(op.f('ix_share_file_uid'), table_name='share_file')
    op.drop_index(op.f('ix_share_file_is_dir'), table_name='share_file')
    op.drop_index(op.f('ix_share_file_indexed'), table_name='share_file')
    op.drop_index(op.f('ix_share_file_file_type'), table_name='share_file')
    op.drop_index(op.f('ix_share_file_feed_type'), table_name='share_file')
    op.drop_table('share_file')
    # ### end Alembic commands ###
