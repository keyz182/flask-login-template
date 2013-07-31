from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
permission = Table('permission', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', Text, nullable=False),
    Column('email', String(length=120)),
    Column('password', Text, nullable=False),
    Column('active', Boolean, nullable=False, default=ColumnDefault(True)),
)

user_permissions = Table('user_permissions', post_meta,
    Column('permission_id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer, primary_key=True, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['permission'].create()
    post_meta.tables['user'].create()
    post_meta.tables['user_permissions'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['permission'].drop()
    post_meta.tables['user'].drop()
    post_meta.tables['user_permissions'].drop()
