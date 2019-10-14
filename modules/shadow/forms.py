# encoding: utf8
from wtforms import IntegerField
from flask_wtf import Form


class RefreshForm(Form):
    duration = IntegerField("Refresh duration(min)")

