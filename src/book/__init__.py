from flask import Blueprint
from flask_restx import Api

from src.book.controller.book_controller import api as book_ns

bp = Blueprint("book", __name__, url_prefix='/book')

# Book API
api = Api(
    bp,
    title="Book API",
    version="1.0.0",
    description="all the API for book",
)

# Registering a Blueprint will also register its routes
api.add_namespace(book_ns, path="/api/v1")
