__author__ = 'keyz'
BOOTSTRAP_USE_CDN = True
BOOTSTRAP_USE_MINIFIED = True
BOOTSTRAP_FONTAWESOME = True

ENABLED_VIEWS = [
    'app.blueprints.home',
    'app.blueprints.auth',
#    'app.blueprints.querybuilder',
#    'app.blueprints.overviewer',
]

CSRF_ENABLED = True
SECRET_KEY = 'insiProject2013'

DEBUG_TB_INTERCEPT_REDIRECTS=False

#SQLALCHEMY_ECHO=True

DEBUG_TB_PANELS = [
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
    ]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

from datetime import timedelta
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['keyz182@gmail.com']

DEBUG = True