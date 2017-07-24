# Copyright (C) 2017 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""
Update workflow related DB tables for workflow-patch1 release

Create Date: 2017-07-24 18:03:38.781339
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '545d1c7adca5'
down_revision = '59aaa4750320'


def upgrade():
  """Upgrade database schema and/or data, creating a new revision."""
  # Add new columns to 'workflows' table
  op.add_column('workflows', sa.Column('repeat_every', sa.Integer,
                                       nullable=True, default=None))


def downgrade():
  """"Downgrade database schema and/or data back to the previous revision."""
  op.drop_column('workflows', 'repeat_every')
