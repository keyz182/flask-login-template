__author__ = 'Kieran'
from functools import update_wrapper

from flask import current_app, abort
from flask.ext.login import current_user


def authorized(checker):
    """Check if current user is authenticated and authorized.

    Meant to be used inside views and templates to protect part of resources.
    """
    return current_user.is_authenticated() and checker()


def require(checker):
    """
    Ensure that current user is authenticated and authorized to access the
    decorated view.  For example::

        @app.route('/protected')
        @require(Any(IsUser('root'), InGroups('admins')))
        def protected():
            pass

    """
    def decorator(fn):
        def wrapped_function(*args, **kwargs):
            if not current_user.is_authenticated():
                return current_app.login_manager.unauthorized()
            if not checker():
                abort(403)
            return fn(*args, **kwargs)
        return update_wrapper(wrapped_function, fn)
    return decorator


class IsUser(object):
    """Check if current user has provided username."""

    def __init__(self, username):
        self.username = username

    def __call__(self):
        return current_user.username == self.username


class HasPermissions(object):
    """Check if current user has provided permissions."""

    def __init__(self, *args):
        self.permissions = set(args)

    def __call__(self):
        return self.permissions <= current_user.has_permissions()


class All(object):
    """Compound checker to check if all provided checkers are true."""

    def __init__(self, *args):
        self.checkers = args

    def __call__(self):
        return all(c() for c in self.checkers)


class Any(object):
    """Compound checker to check if any of provided checkers is true."""

    def __init__(self, *args):
        self.checkers = args

    def __call__(self):
        return any(c() for c in self.checkers)