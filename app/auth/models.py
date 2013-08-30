__author__ = 'keyz'
'''SQLAlchemy Models
    Models used in SQL
'''

from sqlalchemy.orm import *
from flask.ext.login import UserMixin

from app import db
from app.auth.hash_passwords import check_hash, make_hash



group_permission = db.Table('group_permission',
    db.Column('group_id', db.Integer,
           db.ForeignKey('groups.id', onupdate='CASCADE', ondelete='CASCADE'),
           primary_key=True),
    db.Column('permission_id', db.Integer,
           db.ForeignKey('permissions.id', onupdate='CASCADE', ondelete='CASCADE'),
           primary_key=True)
)

user_group = db.Table('user_group',
   db.Column('group_id',db.Integer,
                db.ForeignKey('groups.id', onupdate='CASCADE', ondelete='CASCADE'),
                primary_key=True),
   db.Column('user_id',db.Integer,
                db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'),
                primary_key=True)
)

class User(UserMixin ,  db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.String(120), unique = True)
    _password = db.Column('password', db.Text, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    groups = db.relationship('Group', secondary=user_group, collection_class=set,
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

    def in_groups(self):
        """Return set of groups which user belongs to."""
        perms = set(r.name for r in Group.query.join(Group.users).filter(User.id == self.id).all())
        return perms

    def has_permissions(self):
        """Return set of permissions which user has."""
        perms = set(r.name for r in Permission.query.join(Permission.groups, Group.users).filter(User.id == self.id).all())
        return perms


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)

    permissions = db.relationship('Permission', secondary=group_permission, collection_class=set,
                                    backref=db.backref('groups', collection_class=set, lazy='dynamic'))

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id,
                                 self.name)


class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<%s(%r, %r)>' % (self.__class__.__name__, self.id,
                                 self.name)
