from flask import Blueprint

bp = Blueprint('main', __name__)

# Registering a Blueprint will also register its routes
from src.main import routes