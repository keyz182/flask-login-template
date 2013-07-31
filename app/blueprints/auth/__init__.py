__author__ = 'Kieran'

from flask import Blueprint
from Login import LoginView
from Logout import LogoutView

auth = Blueprint('auth', __name__, template_folder='templates/auth')
auth.add_url_rule('/login', view_func=LoginView.as_view('login'))
auth.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))

from app import lm
lm.login_view = 'auth.login'

class View:
    def get_blueprint(self):
        return auth