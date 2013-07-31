__author__ = 'Kieran'

from flask import Blueprint
from Home import HomeView

home = Blueprint('home', __name__, template_folder='templates/home')
home.add_url_rule('/', view_func=HomeView.as_view('home'))

class View:
    def get_blueprint(self):
        return home