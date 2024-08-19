from src.extensions import db


# AUTHOR Model
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"
