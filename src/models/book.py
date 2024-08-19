from src.extensions import db


# BOOK Model
class Book(db.Model):
    __tablename__ = 'book'
    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    language = db.Column(db.String, nullable=False)
    number_of_copies_available = db.Column(db.Integer, nullable=False)
    book_cover_image = db.Column(db.String)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Book(isbn='{self.isbn}', title='{self.title}', publisher='{self.publisher}', edition={self.edition}, publication_date={self.publication_date})>"


