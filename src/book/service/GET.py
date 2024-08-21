import requests
from collections import defaultdict


from src.extensions import db
from src.models.book import Book
from src.models.book_author import BookAuthor
from src.models.author import Author
from src.models.book_genre import BookGenres
from src.models.book_copy import BookCopy 
from src.models.genre import Genre

# ? ==========================================================================
# ? Utility Function
def fill_authors_list(book_dict: defaultdict, isbn: str) -> None:
    # Get the list of authors id according to the isbn
    list_of_authors = db.session.query(Author) \
        .join(BookAuthor, BookAuthor.author_id == Author.id) \
        .filter(BookAuthor.isbn == isbn) \
        .all()
    
    # Append to the authors list
    for author in list_of_authors:
        book_dict["authors"].append(author.name)


def fill_genres_list(book_dict: defaultdict, isbn: str) -> None:
    # Get the list of genre according to the isbn
    list_of_genres = db.session.query(BookGenres) \
        .filter(BookGenres.isbn == isbn) \
        .all()
    
    # Append to the genres list
    for genre in list_of_genres:
        book_dict['genres'].append(genre.genre)

def fill_shelf_location_list(book_dict: defaultdict, isbn: str) -> None:
    # Get the list of shelf_location according to the isbn
    list_of_shelf_locations = db.session.query(BookCopy) \
        .filter(BookCopy.isbn == isbn) \
        .all()
    
    # Append to the shelf_locations list
    for shelf_location in list_of_shelf_locations:
        book_dict['shelf_locations'].append({
            'book_id': shelf_location.id,
            'shelf': shelf_location.shelf_location,
            'status': shelf_location.book_status,
        })

# ? ==========================================================================
# ? GET methods
"""_summary_
        This GET request will handle for viewing the brief review for all the books
        
    Returns:
    {
        "books": [
            {
                "title": None,
                "edition": None,
                "Language": None,
                "book_cover_image": None,
                "description": None,
                "genres": ["horror", "detective"],
                "authors": ["", ""],
                "shelf_locations": [
                    {"A1": "Available"},
                    {"A2": "Checked out"},
                    {"A3": "Damaged"},
                ]
            },
            {

            }
        ]
    }
"""
def get_all_books(page: int, per_page: int) -> list[dict]:
    # Get all the books
    books = Book.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False,
    ).items

    # Create a dictionary to hold the aggregate results
    books_dict = defaultdict(
        lambda: {
            'ISBN': None,
            "title": None,
            "edition": None,
            "language": None,
            "book_cover_image": None,
            "description": None,
            "genres": [],
            "authors": [],
            "shelf_locations": [],
        }
    )

    # Populate into the books_dict
    for book in books:
        isbn = book.isbn

        books_dict[isbn].update({
            'ISBN': book.isbn,
            "title": book.title,
            "edition": book.edition,
            "language": book.language,
            "book_cover_image": book.book_cover_image,
            "description": book.description,
            "genres": [],
            "authors": [],
            "shelf_locations": [],
        })

        # Fill the Authors List
        fill_authors_list(book_dict=books_dict[isbn], isbn=isbn)

        # Fill the Genres List
        fill_genres_list(book_dict=books_dict[isbn], isbn=isbn)

        # Fill the shelf_location list
        fill_shelf_location_list(book_dict=books_dict[isbn], isbn=isbn)    

    # Convert the defaultdict to a regular list of dictionaries
    books_list = list(books_dict.values())

    return books_list


"""_summary_
        This GET request will handle for viewing detail information a book
        
    Returns:
    {
        "ISBN": ,
        "authors": ["", ""],
        "genres": ["", ""],
        "title": ,
        "publisher": ,
        "edition": ,
        "publication_date": ,
        "language": ,
        "number_of_copies_available": 3,
        "book_cover_image": ,
        "description": ,
        "shelf_locations": [
            {"A1": "Available"},
            {"A2": "Checked out"},
            {"A3": "Damaged"},
        ]
    }
"""
def get_a_book(ISBN: str) -> dict:
    # Get that book
    book: Book = Book.query.filter(
        Book.isbn == ISBN,
    ).first_or_404(description="Book not exist.")
    
    book_dict = defaultdict(lambda: None)
        
    # Populate the book_dict with data
    book_dict.update({
        'ISBN': book.isbn,
        'authors': [],
        'genres': [],
        'title': book.title,
        'publisher': book.publisher,
        'edition': book.edition,
        'publication_date': book.publication_date,
        'language': book.language,
        'number_of_copies_available': book.number_of_copies_available,
        'book_cover_image': book.book_cover_image,
        'description': book.description,
        'shelf_locations': [],
    })
    
    # Fill the Authors List
    fill_authors_list(book_dict, isbn=ISBN)
        
    # Fill the Genres List
    fill_genres_list(book_dict, isbn=ISBN)
    
    # Fill the shelf_location list
    fill_shelf_location_list(book_dict, isbn=ISBN)  
    
    return book_dict


def search_book_by_query(query: str) -> list[dict]:    
    query_like_statement = f'%{query}%'
    
    # Search by title
    books_by_title = Book.query \
        .filter(Book.title.like(query_like_statement)) \
        .all()

            
    # Search by description
    books_by_description = Book.query \
        .filter(Book.description.ilike(query_like_statement)) \
        .all()
    
    # Search by ISBN
    books_by_isbn = Book.query \
        .filter(Book.isbn.ilike(query_like_statement)) \
        .all()
    
    # Search by author name
    books_by_author = db.session.query(Book) \
        .join(BookAuthor, BookAuthor.isbn == Book.isbn) \
        .join(Author, Author.id == BookAuthor.author_id) \
        .filter(Author.name.ilike(query_like_statement)) \
        .all()
        
    # Combine results, remove duplicates
    results = set(books_by_title + books_by_description + books_by_isbn + books_by_author)
    
    # Create a dictionary to hold the aggregate results
    books_dict = defaultdict(
        lambda: {
            'ISBN': None,
            "title": None,
            "edition": None,
            "language": None,
            "book_cover_image": None,
            "description": None,
            "genres": [],
            "authors": [],
            "shelf_locations": [],
        }
    )

    # Populate into the books_dict
    for book in results:
        isbn = book.isbn

        books_dict[isbn].update({
            'ISBN': book.isbn,
            "title": book.title,
            "edition": book.edition,
            "language": book.language,
            "book_cover_image": book.book_cover_image,
            "description": book.description,
            "genres": [],
            "authors": [],
            "shelf_locations": [],
        })

        # Fill the Authors List
        fill_authors_list(book_dict=books_dict[isbn], isbn=isbn)

        # Fill the Genres List
        fill_genres_list(book_dict=books_dict[isbn], isbn=isbn)

        # Fill the shelf_location list
        fill_shelf_location_list(book_dict=books_dict[isbn], isbn=isbn)    

    # Convert the defaultdict to a regular list of dictionaries
    books_list = list(books_dict.values())

    return books_list


def get_book_title_by_isbn(isbn: str):
    # URL-encode the string
    # encoded_isbn = quote(isbn)
    
    read_isbn_api = f'https://openlibrary.org/isbn/{isbn}'
    print(read_isbn_api)
    headers = {
        "accept": "application/json"
    }
    
    response = requests.get(read_isbn_api, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
        return {
            "message": "Invalid ISBN",
            "book_title": "None"
        }, 404
    
    
    # Get the json data
    json_data: dict = response.json()
    print(json_data)
    # Check for the title
    book_title_with_that_isbn = json_data['title'] 
    return {
        "message": "Valid ISBN",
        "book_title": f"{book_title_with_that_isbn}"
    }, 200
    

def get_all_genres(page: int, per_page: int):
    genres = Genre.query \
        .order_by(Genre.genre.asc()) \
        .paginate(page=page, per_page=per_page, error_out=False)
    
    # Return only the genre names as a list
    genres = [genre.genre for genre in genres.items]
    
    return {'genres': genres}, 200


def get_books_filter_by_genres(data: dict, page: int, per_page: int):
    genres = data.get('genres', [])
    if not genres:
        return {"message": "No genres provided"}, 400
    
    # Query books that match the genres
    books_query = Book.query \
        .join(BookGenres, Book.isbn == BookGenres.isbn) \
        .filter(BookGenres.genre.in_(genres)) \
        .paginate(page=page, per_page=per_page, error_out=False)
        
    books = books_query.items
    
    if not books:
        return {"message": "No books found for the given genres"}, 404
    
    # Convert books into the expected output format
    book_list = []
    for book in books:
        book_dict = { 
            "ISBN": book.isbn,
            "title": book.title,
            "edition": book.edition,
            "language": book.language,
            "book_cover_image": book.book_cover_image,
            "description": book.description,
            "genres": [],
            "authors": [],
            "shelf_locations": []
        }
        
        # Fill the Authors List
        fill_authors_list(book_dict=book_dict, isbn=book.isbn)

        # Fill the Genres List
        fill_genres_list(book_dict=book_dict, isbn=book.isbn)

        # Fill the shelf_location list
        fill_shelf_location_list(book_dict=book_dict, isbn=book.isbn)    
        
        # Append to the book_list
        book_list.append(book_dict)
        

    return book_list, 200
    