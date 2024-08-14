from flask import Blueprint

bp = Blueprint('main', __name__)

# Register the Routes
from src.main import routes