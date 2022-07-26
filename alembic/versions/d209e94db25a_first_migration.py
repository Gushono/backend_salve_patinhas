"""first_migration

Revision ID: d209e94db25a
Revises: 
Create Date: 2022-11-29 14:59:56.074125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd209e94db25a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('s3_link', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_picture_id'), 'tb_picture', ['id'], unique=False)
    op.create_table('tb_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('document_number', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_user_id'), 'tb_user', ['id'], unique=False)
    op.create_table('tb_animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_picture', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('specie', sa.String(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_picture'], ['tb_picture.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_animal_id'), 'tb_animal', ['id'], unique=False)
    op.create_table('tb_animal_location_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_picture', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_picture'], ['tb_picture.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_animal_location_model_id'), 'tb_animal_location_model', ['id'], unique=False)
    op.create_table('tb_user_animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_animal', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_animal'], ['tb_animal.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_user_animal_id'), 'tb_user_animal', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tb_user_animal_id'), table_name='tb_user_animal')
    op.drop_table('tb_user_animal')
    op.drop_index(op.f('ix_tb_animal_location_model_id'), table_name='tb_animal_location_model')
    op.drop_table('tb_animal_location_model')
    op.drop_index(op.f('ix_tb_animal_id'), table_name='tb_animal')
    op.drop_table('tb_animal')
    op.drop_index(op.f('ix_tb_user_id'), table_name='tb_user')
    op.drop_table('tb_user')
    op.drop_index(op.f('ix_tb_picture_id'), table_name='tb_picture')
    op.drop_table('tb_picture')
    # ### end Alembic commands ###
