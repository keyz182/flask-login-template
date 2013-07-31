__author__ = 'Kieran'
from flask.ext.wtf import Form, TextField, BooleanField,PasswordField
from flask.ext.wtf import Required

class LoginForm(Form):
    username = TextField('username', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)