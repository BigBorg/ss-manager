# encoding: utf8
from flask import Blueprint, session, abort, render_template, redirect, url_for
from .forms import LoginForm
from settings import SUPER_USER, SUPER_USER_PASSWORD

bp = Blueprint("authentication", __name__, url_prefix="/authentication", template_folder="authentication")


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == SUPER_USER and form.password.data == SUPER_USER_PASSWORD:
            session["user"] = SUPER_USER
            return redirect(url_for("shadow.status"))
        else:
            abort(401)

    else:
        return render_template("authentication/login.html", form=form)

