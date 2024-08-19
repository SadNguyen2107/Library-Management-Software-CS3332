from src.extensions import db


# BOOK_AUTHOR Model
class BookAuthor(db.Model):
    __tablename__ = 'book_author'
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)

    def __repr__(self):
        return f"<BookAuthor(isbn='{self.isbn}', author_id={self.author_id})>"
