from src.models.user import User

def get_all_user():
    return User.query.all()