#!flask/bin/python
# Set the path
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..//')))
sys.path.append('/home/ubuntu/interviewer/')

from flask.ext.script import Manager, Server
from app import *

manager = Manager(app)

#Start up in non-debug mode
manager.add_command("runserver", Server(
    use_debugger=False,
    use_reloader=False,
    host='127.0.0.1',
    port=5000,
    threaded=True))

# Turn on debugger and reloader
manager.add_command("debugserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='127.0.0.1',
    port=5000,
    threaded=False,
    processes=1))

#Reset the user DB
from dbutils.db_reset import ResetDB
@manager.command
def resetdb():
    "Reset the user database to defaults"
    with app.app_context():
        ResetDB()

#Create the user DB
from dbutils.db_create import CreateDB
@manager.command
def createdb():
    "Create the user database"
    with app.app_context():
        CreateDB()

#Downgrade the user DB
from dbutils.db_downgrade import DowngradeDB
@manager.command
def downgradedb():
    "Downgrade the user database"
    with app.app_context():
        DowngradeDB()

#Upgrade the user DB
from dbutils.db_upgrade import UpgradeDB
@manager.command
def upgradedb():
    "Upgrade the user database"
    with app.app_context():
        UpgradeDB()

#Migrate the user DB
from dbutils.db_migrate import MigrateDB
@manager.command
def migratedb():
    "Migrate the user database to the latest version"
    with app.app_context():
        MigrateDB()

#Populate the user DB with test Data
from dbutils.db_init import InitDB
@manager.command
def initdb():
    "Initialise the user database with test data"
    with app.app_context():
        InitDB()

if __name__ == "__main__":
    manager.run()
