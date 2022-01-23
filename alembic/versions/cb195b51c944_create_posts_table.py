"""Create posts table

Revision ID: cb195b51c944
Revises: 
Create Date: 2022-01-22 19:38:49.556338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb195b51c944'
down_revision = None
branch_labels = None
depends_on = None


# alembic revision --autogenerate   =>  automatically generates a revision with the misisng data
# that were newly added to the models

def upgrade():
    op.create_table("posts", sa.Column(
        "id", sa.Integer(), nullable=False, primary_key=True), sa.Column(
        "title", sa.String(), nullable=False))
    # op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=[
    #                       "user_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    # op.drop_contraint("post_users_fk", table_name="posts")
    op.drop_table("posts")
