from src.extensions import db


# RESERVATION_STATUS Model
class ReservationStatus(db.Model):
    __tablename__ = 'reservation_status'
    status = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<ReservationStatus(status='{self.status}', description='{self.description}')>"
