from src.extensions import db


# RESERVATION Model
class Reservation(db.Model):
    __tablename__ = 'reservation'
    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_copy.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    reservation_date = db.Column(db.Date, nullable=False, default=date.today)
    expiration_date = db.Column(db.Date, nullable=False)
    reservation_status = db.Column(db.String(50), db.ForeignKey('reservation_status.status', onupdate="CASCADE", ondelete="SET NULL"), default='Active')

    # Ensure expiration_date is after reservation_date
    __table_args__ = (
        db.CheckConstraint('expiration_date > reservation_date', name='check_reservation_dates'),
    )

    def __repr__(self):
        return f"<Reservation(reservation_id={self.reservation_id}, book_id={self.book_id}, borrower_id={self.borrower_id}, reservation_date={self.reservation_date}, expiration_date={self.expiration_date}, reservation_status='{self.reservation_status}')>"
