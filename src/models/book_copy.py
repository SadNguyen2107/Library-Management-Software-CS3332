from src.extensions import db
from src.models.book_status import BookStatus

class BookCopy(db.Model):
    __tablename__ = "BOOK_COPY"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String, db.ForeignKey("BOOK.isbn"), nullable=False)
    shelf_location = db.Column(db.String, nullable=False, unique=True)
    book_status = db.Column(
        db.String(10), 
        db.ForeignKey("BOOK_STATUS.status"), 
        default="Available",
    )

    def __repr__(self):
        return f"<BookCopy(id={self.id}, isbn='{self.isbn}', shelf_location='{self.shelf_location}', book_status='{self.book_status}')>"
