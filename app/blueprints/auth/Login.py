__author__ = 'Kieran'
from flask import render_template, flash, redirect, request, session
from flask.views import MethodView

from app.auth.models import *

from flask.ext.login import login_user, current_user
from LoginForm import LoginForm


class LoginView(MethodView):
    def get(self):
        if current_user.is_authenticated():
            return redirect(request.args.get('next') or '/')
        form = LoginForm()
        return render_template('auth/login.html',
            title = 'Sign In',
            form = form)

    def post(self):
        if current_user.is_authenticated():
            return redirect(request.args.get('next') or '/')
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None and user.valid_password(form.password.data):
                if login_user(user, remember=form.remember_me.data):
                    # Enable session expiration only if user hasn't chosen to be
                    # remembered.
                    session.permanent = not form.remember_me.data
                    flash('Logged in successfully!', 'success')
                    session['remember_me'] = form.remember_me.data
                    return redirect(request.args.get('next') or '/')
                else:
                    flash('This username is disabled!', 'error')
            else:
                flash('Wrong username or password!', 'error')
        return render_template('auth/login.html',
            title = 'Sign In',
            form = form)