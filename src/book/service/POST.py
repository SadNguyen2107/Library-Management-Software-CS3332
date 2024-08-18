import requests
from datetime import datetime, date
from flask import json
from sqlalchemy import exc

from src.extensions import db
from src.models.book import Book
from src.models.book_author import BookAuthor
from src.models.author import Author
from src.models.book_genre import BookGenre
from src.models.book_copy import BookCopy 


def save_new_book(data: json):    
    try:
        # Start a transaction
        db.session.begin_nested()
        with db.session.no_autoflush:
        
            # Get the book if it has the same ISBN
            book: Book | None = Book.query \
                .filter(Book.isbn == data["ISBN"]) \
                .first()

            # If book exists -> Throw Error
            if book is not None:
                response_object = {
                    "status": "fail",
                    "message": "Book already exists.",
                }
                return response_object, 409

            # Check whether that ISBN whether is valid
            read_isbn_api = f'https://openlibrary.org/isbn/{data['ISBN']}'
            headers = {
                "accept": "application/json"
            }
            
            response = requests.get(read_isbn_api, headers=headers)
            
            # Check if the request was successful
            if response.status_code != 200:
                print(f"Request failed with status code: {response.status_code}")
                print(response.text)
                return {
                    "message": "ISBN does not match with book_title.",
                }, 404
            
            
            # Get the json data
            json_data: dict = response.json()

            # Check for the title
            book_title_with_that_isbn = json_data['title']     
            if 'title' in data:      
                if book_title_with_that_isbn != data['title']:    
                    return {
                        "message": "That book_title does not have that ISBN.",
                        "hint": f"Do you mean book_title `{book_title_with_that_isbn}`."
                    }, 404
            
            
            # Convert publication_date to a Python date object
            if 'publication_date' in data:
                try:
                    publication_date: date = datetime.strptime(data['publication_date'], '%Y-%m-%d').date()
                except ValueError as e:
                    return {"message": f"Invalid date format for publication_date: {str(e)}"}, 400


            # Validate the number of shelf locations
            if len(data['shelf_locations']) != data['number_of_copies_available']:
                response_object = {
                    "status": "fail",
                    "message": "The number of shelf locations must match the number of copies available.",
                }
                return response_object, 400

            # Check shelf_locations
            if 'shelf_locations' in data:
                for shelf_location in data['shelf_locations']:
                    location = shelf_location.get('shelf')
                    status = shelf_location.get('status', 'Available')

                    # Check if the shelf location is occupied
                    if BookCopy.query.filter_by(shelf_location=location).first():
                        return {
                            "message": f"Shelf location {location} is already occupied."
                        }, 400
                        
            
            # If not exist -> Add that book
            # Add to the BOOK table
            new_book: Book = Book(
                isbn=data["ISBN"], 
                title=data["title"],
                publisher=data['publisher'],
                edition=data['edition'],
                publication_date=publication_date,
                language=data['language'],
                number_of_copies_available=data['number_of_copies_available'],
                book_cover_image=data['book_cover_image'],
                description=data['description'],
            )
            db.session.add(new_book)


            # Add to the AUTHOR table and BOOK_AUTHOR table
            if 'authors' in data:
                for author_name in data['authors']:
                    author = Author.query.filter(Author.name == author_name).first()
                    if not author:
                        # If the author does not exist, create a new one
                        author = Author(name=author_name)
                        db.session.add(author)
                        db.session.flush()  # To get the author ID before committing

                    # Create a relationship in the BOOK_AUTHOR table
                    new_book_author = BookAuthor(isbn=data['ISBN'], author_id=author.id)
                    db.session.add(new_book_author)


            # Add to the BOOK_GENRES table
            if 'genres' in data:
                for genre_name in data['genres']:
                    new_book_genre = BookGenre(isbn=data['ISBN'], genre=genre_name)
                    db.session.add(new_book_genre)

            # Add to the BOOK_COPY table
            if 'shelf_locations' in data:
                for shelf_location in data['shelf_locations']:
                    location = shelf_location.get('shelf')
                    status = shelf_location.get('status', 'Available')
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

    except exc.SQLAlchemyError as e:
        # Rollback the transaction if there is an error
        db.session.rollback()
        print(f"Error: {e}")
        return {"message": str(e)}, 500
    
    except Exception as e:
        return {
            "message": f"{e}"
        }, 500