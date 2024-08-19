from src.extensions import db
from src.models.book_status import BookStatus

# BOOK_COPY Model
class BookCopy(db.Model):
    __tablename__ = 'book_copy'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    shelf_location = db.Column(db.String, nullable=False, unique=True)
    book_status = db.Column(db.String(50), db.ForeignKey('book_status.status', onupdate="CASCADE", ondelete="SET NULL"), default='Available')


    def __repr__(self):
        return f"<BookCopy(id={self.id}, isbn='{self.isbn}', shelf_location='{self.shelf_location}', book_status='{self.book_status}')>"
