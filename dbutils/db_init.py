__author__ = 'Kieran'
from app import db, models
from app.models import *

def InitDB():
    print "Pre-populating DB"
    p1 = Permission(name=u'read')
    p2 = Permission(name=u'write')
    p3 = Permission(name=u'delete')
    u1 = User(username=u'admin', password=u'adminpass',email='admin@example.com')
    u2 = User(username=u'foo', password=u'bar')
    u3 = User(username=u'baz', password=u'foobar', active=False)
    p1.users = set([u1, u2, u3])
    p2.users = set([u1,u2])
    p3.users = set([u1])
    db.session.add_all([u1,u2,u3])
    db.session.commit()
    users = models.User.query.all()
