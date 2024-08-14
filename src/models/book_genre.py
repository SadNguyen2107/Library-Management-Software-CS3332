from src.extensions import db


class BookGenre(db.Model):
    __tablename__ = "BOOK_GENRES"
    
    isbn = db.Column(db.String, db.ForeignKey("BOOK.isbn"), primary_key=True)
    genre = db.Column(db.String(10), db.ForeignKey("GENRE.genre"), primary_key=True)

    def __repr__(self):
        return f"<BookGenre(isbn='{self.isbn}', genre='{self.genre}')>"
