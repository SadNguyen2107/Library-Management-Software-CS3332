from src.extensions import db


class Genre(db.Model):
    __tablename__ = "GENRE"

    genre = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String)

    def __repr__(self):
        return f"<Genre(genre='{self.genre}', description='{self.description}')>"
