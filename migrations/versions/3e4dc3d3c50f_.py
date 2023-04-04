"""empty message

Revision ID: 3e4dc3d3c50f
Revises: 
Create Date: 2023-03-07 00:09:14.114868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e4dc3d3c50f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('farmlands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('croptype_id', sa.Integer(), nullable=True),
    sa.Column('sow_date', sa.Date(), nullable=True),
    sa.Column('harvest_date', sa.Date(), nullable=True),
    sa.Column('product_expected', sa.Float(), nullable=True),
    sa.Column('coordinates', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['croptype_id'], ['crops.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('coordinates'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('historicfarmlands',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('current_farm_id', sa.Integer(), nullable=True),
    sa.Column('croptype_id', sa.Integer(), nullable=True),
    sa.Column('sow_date', sa.Date(), nullable=True),
    sa.Column('harvest_date', sa.Date(), nullable=True),
    sa.Column('product_obtained', sa.Float(), nullable=True),
    sa.Column('nitrogen_type1', sa.Float(), nullable=True),
    sa.Column('phosphorus_type1', sa.Float(), nullable=True),
    sa.Column('potassium_type1', sa.Float(), nullable=True),
    sa.Column('posology_type1', sa.Float(), nullable=True),
    sa.Column('nitrogen_type2', sa.Float(), nullable=True),
    sa.Column('phosphorus_type2', sa.Float(), nullable=True),
    sa.Column('potassium_type2', sa.Float(), nullable=True),
    sa.Column('posology_type2', sa.Float(), nullable=True),
    sa.Column('nitrogen_type3', sa.Float(), nullable=True),
    sa.Column('phosphorus_type3', sa.Float(), nullable=True),
    sa.Column('potassium_type3', sa.Float(), nullable=True),
    sa.Column('posology_type3', sa.Float(), nullable=True),
    sa.Column('diseases_abnormalities', sa.String(length=150), nullable=True),
    sa.Column('diseases_abnormalitiesdate', sa.Date(), nullable=True),
    sa.Column('observation', sa.String(length=160), nullable=True),
    sa.ForeignKeyConstraint(['croptype_id'], ['crops.id'], ),
    sa.ForeignKeyConstraint(['current_farm_id'], ['farmlands.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('soilfarmlands',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('current_farm_id', sa.Integer(), nullable=True),
    sa.Column('soil_date', sa.Date(), nullable=True),
    sa.Column('soil_depth', sa.Float(), nullable=True),
    sa.Column('soil_organic_level', sa.Float(), nullable=True),
    sa.Column('phosphorus', sa.Float(), nullable=True),
    sa.Column('potassium', sa.Float(), nullable=True),
    sa.Column('calcium', sa.Float(), nullable=True),
    sa.Column('phosphorus_unit_id', sa.Integer(), nullable=False),
    sa.Column('potassium_unit_id', sa.Integer(), nullable=False),
    sa.Column('calcium_unit_id', sa.Integer(), nullable=False),
    sa.Column('sand', sa.Float(), nullable=True),
    sa.Column('slit', sa.Float(), nullable=True),
    sa.Column('clay', sa.Float(), nullable=True),
    sa.Column('sulfur', sa.Float(), nullable=True),
    sa.Column('magnesium', sa.Float(), nullable=True),
    sa.Column('boron', sa.Float(), nullable=True),
    sa.Column('copper', sa.Float(), nullable=True),
    sa.Column('zinc', sa.Float(), nullable=True),
    sa.Column('manganese', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['calcium_unit_id'], ['units.id'], ),
    sa.ForeignKeyConstraint(['current_farm_id'], ['farmlands.id'], ),
    sa.ForeignKeyConstraint(['phosphorus_unit_id'], ['units.id'], ),
    sa.ForeignKeyConstraint(['potassium_unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('soilfarmlands')
    op.drop_table('historicfarmlands')
    op.drop_table('users')
    op.drop_table('farmlands')
    op.drop_table('units')
    op.drop_table('roles')
    op.drop_table('crops')
    # ### end Alembic commands ###
