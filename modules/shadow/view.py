# encoding:utf8
from datetime import timedelta
from flask import Blueprint, render_template
from utils.utils import login_required
from .tasks import status_ss, refresh_ss
from .forms import RefreshForm

bp = Blueprint("shadow", __name__, template_folder="shadow", url_prefix="/shadow")


@bp.route("/index", methods=["GET", "POST"])
@login_required
def status():
    message = ""
    refresh_form = RefreshForm()
    if refresh_form.validate_on_submit():
        refresh_ss.delay(refresh_form.duration.data).get()
        message = "Successfully refresh duration"

    status_info = status_ss.delay().get()
    return render_template("shadow/index.html", refresh_form=refresh_form, message=message, **status_info)

