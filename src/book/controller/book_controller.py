from flask import request
from flask_restx import Resource

from src.book.util.dto import BookDto
from src.book.service.book_service import (
    get_all_books,
    get_a_book_by_ISBN,
    search_book_by_query,
    save_new_book,
)

api = BookDto.api
_book = BookDto.book_dto
_book_detail = BookDto.book_detail_dto

@api.route("/books")
class BookList(Resource):

    @api.doc("List of available books")
    @api.param("page", "The current page", default=1, type=int)
    @api.param("per_page", "The maximum number of items on a page", default=5, type=int)
    @api.marshal_list_with(_book, envelope='books')
    def get(self):
        """List all the available books"""
        # Get query parameter
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=5, type=int)

        return get_all_books(page=page, per_page=per_page)
    

    @api.doc("Add a new book")
    @api.response(201, "Book successfully added.")
    @api.response(400, "The number of shelf locations must match the number of copies available.")
    @api.response(400, "Genre does not exist.")
    @api.response(409, "Book already exists.")
    @api.expect(_book_detail, validate=True)
    def post(self):
        """Add a new book"""
        data = request.json
        return save_new_book(data=data)



@api.route('/search')
class SearchBook(Resource):
    
    @api.doc("Search all available books")
    @api.param("query", "Enter something to search books", type=str, required=True)
    @api.marshal_list_with(_book, envelope='books')
    def get(self):
        """Search books"""
        # Get query parameter
        query = request.args.get("query", default="", type=str)

        return search_book_by_query(query)



@api.route("/<ISBN>")
@api.param("ISBN", "The Book ISBN", type=str)
@api.response(404, "Book not found.")
class Book(Resource):

    @api.doc("Get a book.")
    @api.marshal_with(_book_detail)
    def get(self, ISBN):
        """Get a book given its ISBN"""
        return get_a_book_by_ISBN(ISBN=ISBN)
