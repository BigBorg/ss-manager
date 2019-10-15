import functools
from flask import session, abort
from settings import SUPER_USER


def login_required(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        if session.get("user", "") == SUPER_USER:
            return fn(*args, **kwargs)
        else:
            abort(401)

    return wrapped
