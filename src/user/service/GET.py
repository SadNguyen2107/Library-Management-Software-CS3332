from src.models.user import User


def get_all_users():
    return User.query.all()    


def get_a_user(user_id: int):
    pass


def get_borrowed_history(user_id: int):
    pass