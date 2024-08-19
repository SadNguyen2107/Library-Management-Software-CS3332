from src.extensions import db


# GENRE Model
class Genre(db.Model):
    __tablename__ = 'genre'
    genre = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Genre(genre='{self.genre}', description='{self.description}')>"
