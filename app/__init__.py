__author__ = 'keyz'
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from .auth import authorized
from flask_debugtoolbar import DebugToolbarExtension
from app.blueprints import register_blueprints

app = Flask(__name__)
app.config.from_object('config')

app.debug = True

#Enable Bootstrap
Bootstrap(app)

#Enable SQLAchemy
db = SQLAlchemy(app)

#Enable Flask-login
lm = LoginManager()
lm.login_view = 'login'
lm.init_app(app)

app.jinja_env.globals['authorized'] = authorized

#if debugging is enabled, add the debug toolbar
if app.debug:
    toolbar = DebugToolbarExtension(app)

#Register the blueprints from config (ENABLED_VIEWS)
register_blueprints(app)


#Register error handlers
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

#User loader for flask-login
from app.models import *
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

#Log to file if debugging is not enabled
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler('tmp/app.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('???')

if __name__ == '__main__':
    app.run()
