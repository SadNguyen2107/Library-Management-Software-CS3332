from src.extensions import db


class BookAuthor(db.Model):
    __tablename__ = "BOOK_AUTHOR"
    
    isbn = db.Column(db.String, db.ForeignKey("BOOK.isbn"), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("AUTHOR.id"), primary_key=True)

    def __repr__(self):
        return f"<BookAuthor(isbn='{self.isbn}', author_id={self.author_id})>"
