"""
? Extensions.py:
Set up various Flask extensions, to your `src` directory
"""

# TODO: Use SQlAlchemy to do the Query Database with ORM (in the future)
from flask_sqlalchemy import SQLAlchemy
db: SQLAlchemy = SQLAlchemy()


from flask_login import LoginManager
login_manager: LoginManager = LoginManager()


from flask_mail import Mail
mail: Mail = Mail()