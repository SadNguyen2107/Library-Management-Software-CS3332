from src.extensions import db


class Reservation(db.Model):
    __tablename__ = "RESERVATION"

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey("BOOK_COPY.id"), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey("USER.id"), nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    reservation_status = db.Column(
        db.String(10),
        db.ForeignKey("RESERVATION_STATUS.status"),
        default="Active",
    )

    def __repr__(self):
        return f"<Reservation(reservation_id={self.reservation_id}, book_id={self.book_id}, borrower_id={self.borrower_id}, reservation_date={self.reservation_date}, expiration_date={self.expiration_date}, reservation_status='{self.reservation_status}')>"
