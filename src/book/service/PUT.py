from datetime import datetime

import requests
from flask import json
from sqlalchemy import exc

from src.extensions import db
from src.models.book import Book
from src.models.book_author import BookAuthor
from src.models.author import Author
from src.models.book_genre import BookGenres
from src.models.genre import Genre
from src.models.book_copy import BookCopy 
from src.models.deposit import Deposit


"""
_summary_:
    Update the book with ISBN with the new_data
"""

def update_a_book(original_isbn: str, new_data: json):
    try:
        # Start a transaction
        db.session.begin_nested()
        with db.session.no_autoflush:
        
            # Check that book with original_isbn to update
            book = Book.query \
                .filter(Book.isbn == original_isbn) \
                .first_or_404("Book not found.")
                
            # Check whether that ISBN whether is valid
            read_isbn_api = f'https://openlibrary.org/isbn/{new_data["ISBN"]}'
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
            if 'title' in new_data:      
                if book_title_with_that_isbn != new_data['title']:    
                    return {
                        "message": "That book_title does not have that ISBN.",
                        "hint": f"Do you mean book_title `{book_title_with_that_isbn}`."
                    }, 404
                    
            # Check if any copies of the book are currently issued
            active_deposits = db.session.query(Deposit).join(BookCopy).filter(
                BookCopy.isbn == original_isbn, 
                Deposit.return_date == None
            ).count()
            
            if active_deposits > 0:
                return {
                    "message": "Cannot update the book. All copies must be returned first."
                }, 400
            
            # Convert publication_date to a Python date object
            if 'publication_date' in new_data:
                try:
                    book.publication_date = datetime.strptime(new_data['publication_date'], '%Y-%m-%d').date()
                except ValueError as e:
                    return {"message": f"Invalid date format for publication_date: {str(e)}"}, 400
            
            
            # Validate the number of shelf locations
            if len(new_data['shelf_locations']) != new_data['number_of_copies_available']:
                response_object = {
                    "status": "fail",
                    "message": "The number of shelf locations must match the number of copies available.",
                }
                return response_object, 400
            
            # Check shelf_locations
            if 'shelf_locations' in new_data:
                for shelf_location in new_data['shelf_locations']:
                    location = shelf_location.get('shelf')
                    status = shelf_location.get('status', 'Available')

                    # Check if the shelf location is occupied
                    if BookCopy.query.filter_by(shelf_location=location).first():
                        return {
                            "message": f"Shelf location {location} is already occupied."
                        }, 400
            
            
            # Check if the ISBN is being updated
            new_isbn = new_data.get('ISBN', original_isbn)
            
            if new_isbn != original_isbn:
                # Update all related records with the new ISBN
                BookAuthor.query.filter_by(isbn=original_isbn).update({"isbn": new_isbn})
                BookGenres.query.filter_by(isbn=original_isbn).update({"isbn": new_isbn})
                BookCopy.query.filter_by(isbn=original_isbn).update({"isbn": new_isbn})
                Deposit.query.filter(Deposit.book_id.in_(
                    db.session.query(BookCopy.id).filter_by(isbn=original_isbn)
                )).update({"book_id": new_isbn}, synchronize_session=False)

                # Update the ISBN in the book record
                book.isbn = new_isbn
            
            
            # Update other book fields with the new data
            book.title = new_data.get('title', book.title)
            book.publisher = new_data.get('publisher', book.publisher)
            book.edition = new_data.get('edition', book.edition)
            book.language = new_data.get('language', book.language)
            book.number_of_copies_available = new_data.get('number_of_copies_available', book.number_of_copies_available)
            book.book_cover_image = new_data.get('book_cover_image', book.book_cover_image)
            book.description = new_data.get('description', book.description)


            # Update authors
            if 'authors' in new_data:
                BookAuthor.query.filter_by(isbn=new_isbn).delete(synchronize_session=False)
                for author_name in new_data['authors']:
                    author = Author.query.filter_by(name=author_name).first()
                    if not author:
                        author = Author(name=author_name)
                        db.session.add(author)
                        db.session.commit()  # Commit to ensure author_id is available
                    book_author = BookAuthor(isbn=new_isbn, author_id=author.id)
                    db.session.add(book_author)


            # Update genres
            if 'genres' in new_data:
                BookGenres.query.filter_by(isbn=new_isbn).delete(synchronize_session=False)
                for genre_name in new_data['genres']:
                    genre = Genre.query.filter_by(genre=genre_name).first()
                    if not genre:
                        genre = Genre(genre=genre_name)
                        db.session.add(genre)
                    book_genre = BookGenres(isbn=new_isbn, genre=genre.genre)
                    db.session.add(book_genre)


            # Update shelf locations
            if 'shelf_locations' in new_data:
                BookCopy.query.filter_by(isbn=new_isbn).delete(synchronize_session=False)
                for shelf_location in new_data['shelf_locations']:
                    location = shelf_location.get('shelf')
                    status = shelf_location.get('status', 'Available')
                    book_copy = BookCopy(isbn=new_isbn, shelf_location=location, book_status=status)
                    db.session.add(book_copy)


            # Commit the transaction
            db.session.commit()
            return {"message": "Book updated successfully."}, 200
    
    except exc.SQLAlchemyError as e:
        # Rollback the transaction if there is an error
        db.session.rollback()
        print(f"Error: {e}")
        return {"message": str(e)}, 500
