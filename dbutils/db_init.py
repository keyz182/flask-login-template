__author__ = 'Kieran'
from app import db
from app.auth.models import *

def InitDB():
    print "Pre-populating DB"
    p1 = Permission(name=u'read')
    p2 = Permission(name=u'write')
    p3 = Permission(name=u'delete')

    g1 = Group(name=u'Administrator')
    g2 = Group(name=u'Developer')
    g3 = Group(name=u'User')

    u1 = User(username=u'admin', password=u'adminpass',email='admin@example.com')
    u2 = User(username=u'foo', password=u'bar')
    u3 = User(username=u'baz', password=u'foobar', active=False)

    g1.permissions = set([p1,p2,p3])
    g2.permissions = set([p1,p2])
    g3.permissions = set([p1])

    u1.groups = set([g1,g2])
    u2.groups = set([g2])
    u3.groups = set([g3])

    db.session.add_all([u1,u2,u3])
    db.session.commit()

    users = User.query.all()

    for u in users:
        print u
        for g in u.in_groups():
            print '\t%s' % g
        for p in u.has_permissions():
            print '\t\t%s' % p
