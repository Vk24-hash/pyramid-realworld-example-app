"""proper tags.

Revision ID: 54a3f0ecbe4e
Revises: 6781acfc7c14
Create Date: 2019-05-08 23:35:26.048950

"""
from alembic import op
from sqlalchemy.dialects import postgresql

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "54a3f0ecbe4e"
down_revision = "6781acfc7c14"
branch_labels = None
depends_on = None


def upgrade():  # noqa: D103
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "article_tags",
        sa.Column("article_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("tag_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
            name=op.f("fk_article_tags_article_id_articles"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"], ["tags.id"], name=op.f("fk_article_tags_tag_id_tags")
        ),
    )
    # ### end Alembic commands ###


def downgrade():  # noqa: D103
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("article_tags")
    # ### end Alembic commands ###
