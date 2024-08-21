from flask import request
from flask_restx import Resource

from flask_login import login_required
from src.authorization import librarian_required
from src.book.util.dto import BookDto
from src.book.service.GET import (
    get_book_title_by_isbn,
    get_all_books,
    get_a_book,
    search_book_by_query,
    get_all_genres,
    get_books_filter_by_genres,
)
from src.book.service.POST import (
    save_new_book,
)
from src.book.service.PUT import (
    update_a_book,
)
from src.book.service.DELETE import (
    delete_a_book,
)

api = BookDto.api
_book = BookDto.book_dto
_book_detail = BookDto.book_detail_dto
_genre_list = BookDto.genre_list_dto


# BOOK
@api.route('/book')
class Book(Resource):
    
    @api.doc("Add a new book")
    @login_required
    @librarian_required
    @api.response(201, "Book successfully added.")
    @api.response(400, "The number of shelf locations must match the number of copies available.")
    @api.response(400, "Genre not exist.")
    @api.response(409, "Book already exists.")
    @api.expect(_book_detail, validate=True)
    def post(self):
        """Add a new book"""
        data = request.json
        return save_new_book(data=data)
    

@api.route('/book/isbn')
class Isbn(Resource):

    @api.doc("Get book_title givens its ISBN")
    @api.response(200, "Valid ISBN")
    @api.response(404, "Invalid ISBN")
    @api.param("ISBN", "The ISBN to get the book_title", type=str)
    def get(self):
        """Get the book_title given its ISBN"""
        isbn = request.args.get('ISBN', default=None, type=str)
        return get_book_title_by_isbn(isbn)


@api.route('/book/genres')
class Genres(Resource):

    @api.doc("Get all the available genres in the database")
    @api.param("page", "The current page", default=1, type=int)
    @api.param("per_page", "The maximum number of items on a page", default=5, type=int)
    @api.marshal_with(_genre_list)
    def get(self):
        """Get all the available genres in the database"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        return get_all_genres(page, per_page) 
    
    
@api.route('/book/genres/search')
class Genres(Resource):

    @api.doc("Search the books by amount of filter")
    @api.param("page", "The current page", default=1, type=int)
    @api.param("per_page", "The maximum number of items on a page", default=5, type=int)
    @api.expect(_genre_list, validate=True)
    @api.marshal_list_with(_book, envelope='books')
    def post(self):
        """Get all the available genres in the database"""
        data = request.json
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        return get_books_filter_by_genres(data=data, page=page, per_page=per_page)


@api.route("/book/isbn/<string:ISBN>")
@api.param("ISBN", "The Book ISBN", type=str)
@api.response(404, "Book not found.")
class Book(Resource):

    @api.doc("Get a book given its ISBN in the library.")
    @api.marshal_with(_book_detail)
    def get(self, ISBN):
        """Get a book given its ISBN in the library"""
        return get_a_book(ISBN=ISBN)
    
    
    @api.doc("Update the book.")
    @api.response(200, "Book updated successfully.")
    @api.response(400, "Cannot update the book. All copies must be returned first.")
    @api.response(404, "ISBN does not match with book_title.")
    @api.expect(_book_detail, validate=True)
    def put(self, ISBN):
        """Update a book givin its ISBN"""
        data = request.json
        return update_a_book(original_isbn=ISBN, new_data=data)
    
    
    @api.doc("Delete the book")
    @login_required
    @librarian_required
    @api.response(204, "Book deleted.")
    @api.response(400, "Cannot update the book. All copies must be returned first.")
    def delete(self, ISBN):
        """Delete a book given its ISBN"""
        return delete_a_book(ISBN=ISBN)


# BOOKS
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


@api.route('/books/search')
class SearchBook(Resource):
    
    @api.doc("Search all available books")
    @api.param("query", "Enter something to search books", type=str, required=True)
    @api.marshal_list_with(_book, envelope='books')
    def get(self):
        """Search books"""
        # Get query parameter
        query = request.args.get("query", default="", type=str)

        return search_book_by_query(query=query)
