from src.extensions import db


class ReservationStatus(db.Model):
    __tablename__ = "RESERVATION_STATUS"

    status = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<ReservationStatus(status='{self.status}', description='{self.description}')>"
