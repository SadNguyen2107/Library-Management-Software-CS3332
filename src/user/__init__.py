from flask import Blueprint
from flask_restx import Api

from src.user.controller.user_controller import api as user_ns

bp = Blueprint('user', __name__, url_prefix='/user')

# User API
api = Api(
    bp,
    title='User API',
    version='1.0.0',
    description='all the API for the user',
)

# Registering a Blueprint will also register its routes
api.add_namespace(user_ns, path='/api/v1')