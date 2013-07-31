__author__ = 'Kieran'
from flask import flash, redirect
from flask.views import MethodView

from flask.ext.login import logout_user, login_required


class LogoutView(MethodView):
    @login_required
    def get(self):
        logout_user()
        flash('You have logged out!')
        return redirect('/')