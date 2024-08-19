from src.extensions import db

# BOOK_GENRES Model
class BookGenres(db.Model):
    __tablename__ = 'book_genres'
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    genre = db.Column(db.String(50), db.ForeignKey('genre.genre', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)

    def __repr__(self):
        return f"<BookGenre(isbn='{self.isbn}', genre='{self.genre}')>"
