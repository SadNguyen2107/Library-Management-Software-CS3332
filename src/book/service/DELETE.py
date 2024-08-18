from src.extensions import db
from src.models.book import Book
from src.models.book_author import BookAuthor
from src.models.author import Author
from src.models.book_genre import BookGenre
from src.models.book_copy import BookCopy 
from src.models.deposit import Deposit


def delete_a_book(ISBN: str):
    try:
        # Check that book with original_isbn to update
        book = Book.query \
            .filter(Book.isbn == ISBN) \
            .one_or_404("Book not found.")
            
        # Check if any copies of the book are currently issued
        active_deposits = db.session.query(Deposit).join(BookCopy).filter(
            BookCopy.isbn == ISBN, 
            Deposit.return_date == None
        ).count()

        if active_deposits > 0:
            return {
                "message": "Cannot delete the book. All copies must be returned first."
            }, 400
            
        # Delete related records in BookCopy, BookAuthor, and BookGenre tables
        BookCopy.query.filter_by(isbn=ISBN).delete()
        BookAuthor.query.filter_by(isbn=ISBN).delete()
        BookGenre.query.filter_by(isbn=ISBN).delete()
        Deposit.query.filter(Deposit.book_id.in_(
            db.session.query(BookCopy.id).filter_by(isbn=ISBN)
        )).delete(synchronize_session=False)
            
        # Delete the book itself
        db.session.delete(book)
        db.session.commit()
        return '', 204

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500
