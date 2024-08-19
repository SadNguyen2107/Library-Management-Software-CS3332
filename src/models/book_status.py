from src.extensions import db


# BOOK_STATUS Model
class BookStatus(db.Model):
    __tablename__ = 'book_status'
    status = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<BookStatus(status='{self.status}', description='{self.description}')>"
