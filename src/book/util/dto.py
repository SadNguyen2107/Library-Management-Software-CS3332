from flask_restx import Namespace, fields

class BookDto:
    api = Namespace('book', description='book related operations')
    # Define the DTO for a single shelf location
    shelf_location_dto = api.model('ShelfLocation', {
        'book_id': fields.Integer(readonly=True, description='The Book ID in the library'),
        'shelf': fields.String(required=True, description='The book shelf location to put in'),
        'status': fields.String(required=True, description='The status of that book at that shelf_location')
    })

    # Define the DTO for a single book
    book_dto = api.model('Book', {
        'ISBN': fields.String(required=True, description='The ISBN of the book'),
        'title': fields.String(required=True, default=None, description='The title of the book'),
        'edition': fields.String(default=None, description='The edition of the book'),
        'language': fields.String(default=None, description='The language the book is written in'),
        'book_cover_image': fields.String(default=None, description='The URL for the book cover image'),
        'description': fields.String(default=None, description='A brief description of the book'),
        'genres': fields.List(fields.String, description='List of genres associated with the book'),
        'authors': fields.List(fields.String, description='List of authors of the book'),
        'shelf_locations': fields.List(fields.Nested(shelf_location_dto), description='List of shelf locations and their status')
    })
    
    
    book_detail_dto = api.model('BookDetail', {
        'ISBN': fields.String(required=True, description='The ISBN of the book'),
        'authors': fields.List(fields.String, description='List of authors of the book'),
        'genres': fields.List(fields.String, description='List of genres associated with the book'),
        'title': fields.String(required=True, description='The title of the book'),
        'publisher': fields.String(description='The publisher of the book'),
        'edition': fields.String(description='The edition of the book'),
        'publication_date': fields.String(description='The publication date of the book'),
        'language': fields.String(description='The language the book is written in'),
        'number_of_copies_available': fields.Integer(description='Number of copies available in the library'),
        'book_cover_image': fields.String(description='The URL for the book cover image'),
        'description': fields.String(description='A brief description of the book'),
        'shelf_locations': fields.List(fields.Nested(shelf_location_dto), description='List of shelf locations and their status'),
    })
    
    
    genre_list_dto = api.model('GenreList', {
        'genres': fields.List(fields.String, description="List of genre names")
    })