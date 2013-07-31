__author__ = 'Kieran'

def register_blueprints(app):
    from config import ENABLED_VIEWS
    for view in ENABLED_VIEWS:
        klass = __import__(view, fromlist=['View'])
        v = klass.View()
        app.register_blueprint(v.get_blueprint())