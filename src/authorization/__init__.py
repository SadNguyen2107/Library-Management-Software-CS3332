from functools import wraps
from flask import abort
from flask_login import current_user


def librarian_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.user_role != "Librarian":
            abort(403, description="You do not have access to this resource.")
        return f(*args, **kwargs)

    return decorated_function


def own_profile_or_librarian_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = kwargs.get("user_id")
        if current_user.user_role == "Member" and current_user.id != user_id:
            abort(403, description="You do not have access to this resource.")
        return f(*args, **kwargs)

    return decorated_function
