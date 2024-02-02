"""new tables

Revision ID: 581476eb5ef7
Revises: 6eea90f33bda
Create Date: 2024-02-02 10:56:24.734133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '581476eb5ef7'
down_revision = '6eea90f33bda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], name=op.f('fk_item_collections_collection_id_collections')),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_item_collections_item_id_items')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], name=op.f('fk_user_collections_collection_id_collections')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_collections_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('forums')
    with op.batch_alter_table('collections', schema=None) as batch_op:
        batch_op.drop_constraint('fk_collections_item_id_items', type_='foreignkey')
        batch_op.drop_constraint('fk_collections_user_id_users', type_='foreignkey')
        batch_op.drop_column('item_id')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_constraint('fk_comments_user_id_users', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_comments_user_id_users', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('collections', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('item_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_collections_user_id_users', 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key('fk_collections_item_id_items', 'items', ['item_id'], ['id'])

    op.create_table('forums',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('post', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_forums_user_id_users'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_collections')
    op.drop_table('item_collections')
    # ### end Alembic commands ###
