__author__ = 'keyz'
'''SQLAlchemy Models
    Models used in SQL
'''

from app import db
from sqlalchemy.orm import *
from flask.ext.login import UserMixin

from .hash_passwords import check_hash, make_hash


user_permissions = db.Table('user_permissions',
                               db.Column('permission_id',db.Integer,
                                            db.ForeignKey('permission.id', onupdate='CASCADE', ondelete='CASCADE'),
                                            primary_key=True),
                               db.Column('user_id',db.Integer,
                                            db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'),
                                            primary_key=True)
                )

class User(UserMixin ,  db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.String(120), unique = True)
    _password = db.Column('password', db.Text, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    permissions = db.relationship('Permission', secondary=user_permissions, collection_class=set,
                                    backref=db.backref('users', collection_class=set, lazy='dynamic'))

    def _set_password(self, password):
        self._password = make_hash(password)

    def _get_password(self):
        return self._password

    password = synonym('_password', descriptor=property(_get_password,
                                                        _set_password))
    def is_authenticated(self):
        return True

    def valid_password(self, password):
        """Check if provided password is valid."""
        return check_hash(password, self.password)

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id,
                                 self.username)

    def has_permissions(self):
        """Return set of permissions which user has."""
        perms = set(r.name for r in Permission.query.join(Permission.users).filter(User.id == self.id).all())

        return perms

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id,
                                 self.name)

