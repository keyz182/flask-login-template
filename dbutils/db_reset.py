__author__ = 'Kieran'
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
from db_create import CreateDB
from db_init import InitDB

def ResetDB():
    print "Dropping DB Tables"
    db.drop_all()
    print "Dropping DB Version Control"
    api.drop_version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)

    CreateDB()

    InitDB()