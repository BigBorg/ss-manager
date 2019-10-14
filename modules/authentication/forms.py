# encoding: utf8
from wtforms import PasswordField, StringField
from flask_wtf import Form, RecaptchaField


class LoginForm(Form):
    username = StringField("username")
    password = PasswordField("password")
    recaptcha = RecaptchaField()

