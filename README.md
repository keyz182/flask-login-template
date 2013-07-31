# Flask Template Project

## Introduction
This is a Flask template project which utilizes flask-login, and flask-sqlalchemy, along with sqlalchemy-migration.
All code for needed user authorization is in place. By default, an sqlite database is used.


## Installation
On Linux:

```bash
git clone https://github.com/keyz182/flask-login-template.git
cd flask-login-template
virtualenv flask
./flask/bin/pip install -r requirements.txt
./flask/bin/python run.py runserver
```

## Usage

```bash
$ ./flask/bin/python run.py
Please provide a command:
  createdb     Create the user database
  debugserver  Runs the Flask development server i.e. app.run()
  downgradedb  Downgrade the user database
  initdb       Initialise the user database with test data
  migratedb    Migrate the user database to the latest version
  resetdb      Reset the user database to defaults
  runserver    Runs the Flask development server i.e. app.run()
  shell        Runs a Python shell inside Flask application context.
  upgradedb    Upgrade the user database
```