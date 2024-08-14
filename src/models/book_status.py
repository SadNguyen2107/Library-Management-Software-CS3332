from src.extensions import db


class BookStatus(db.Model):
    __tablename__ = "BOOK_STATUS"
    
    status = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<BookStatus(status='{self.status}', description='{self.description}')>"
