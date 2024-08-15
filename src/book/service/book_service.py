from flask import json
from collections import defaultdict

from src.extensions import db
from src.models.book import Book
from src.models.book_author import BookAuthor
from src.models.author import Author
from src.models.book_genre import BookGenre
from src.models.book_copy import BookCopy 

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
    list_of_genres = db.session.query(BookGenre) \
        .filter(BookGenre.isbn == isbn) \
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
            shelf_location.shelf_location: shelf_location.book_status
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
    )

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
def get_a_book_by_ISBN(ISBN: str) -> dict:
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
    # Search by title
    books_by_title = Book.query \
        .filter(Book.title.ilike(f"%{query}%")) \
        .all()
            
    # Search by description
    books_by_description = Book.query \
        .filter(Book.description.ilike(f"%{query}%")) \
        .all()
    
    # Search by ISBN
    books_by_isbn = Book.query \
        .filter(Book.isbn.ilike(f"%{query}%")) \
        .all()
    
    # Search by author name
    books_by_author = db.session.query(Book) \
        .join(BookAuthor, BookAuthor.isbn == Book.isbn) \
        .join(Author, Author.id == BookAuthor.author_id) \
        .filter(Author.name.ilike(f"%{query}%")) \
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

#! ==========================================================================
#! POST methods
def save_new_book(data: json):
    # Get the book if it has the same ISBN
    book: Book | None = Book.query.filter(Book.isbn == data["ISBN"]).first()

    # If book exists -> Throw Error
    if book is not None:
        response_object = {
            "status": "fail",
            "message": "Book already exists.",
        }
        return response_object, 409

    # Validate the number of shelf locations
    if len(data['shelf_locations']) != data['number_of_copies_available']:
        response_object = {
            "status": "fail",
            "message": "The number of shelf locations must match the number of copies available.",
        }
        return response_object, 400

    # If not exist -> Add that book
    # Add to the BOOK table
    new_book: Book = Book(
        isbn=data["ISBN"], 
        title=data["title"],
        publisher=data['publisher'],
        edition=data['edition'],
        publication_date=data['publication_date'],
        language=data['language'],
        number_of_copies_available=data['number_of_copies_available'],
        book_cover_image=data['book_cover_image'],
        description=data['description'],
    )
    db.session.add(new_book)

    # Add to the AUTHOR table and BOOK_AUTHOR table
    for author_name in data['authors']:
        author = Author.query.filter(Author.name == author_name).first()
        if not author:
            # If the author does not exist, create a new one
            author = Author(name=author_name)
            db.session.add(author)
            db.session.flush()  # To get the author ID before committing

        # Create a relationship in the BOOK_AUTHOR table
        new_book_author = BookAuthor(isbn=data['ISBN'], author_id=author.ID)
        db.session.add(new_book_author)

    # Add to the BOOK_GENRES table
    for genre_name in data['genres']:
        genre = BookGenre.query.filter(BookGenre.genre == genre_name).first()
        if not genre:
            # If the genre does not exist, handle this accordingly
            response_object = {
                "status": "fail",
                "message": f"Genre '{genre_name}' does not exist.",
            }
            return response_object, 400

        new_book_genre = BookGenre(isbn=data['ISBN'], genre=genre_name)
        db.session.add(new_book_genre)

    # Add to the BOOK_COPY table
    for shelf_location in data['shelf_locations']:
        for location, status in shelf_location.items():
            new_book_copy = BookCopy(
                isbn=data['ISBN'],
                shelf_location=location,
                book_status=status,
            )
            db.session.add(new_book_copy)

    # Commit all the changes to the database
    db.session.commit()

    response_object = {
        "status": "success",
        "message": "Book successfully added.",
    }
    return response_object, 201


