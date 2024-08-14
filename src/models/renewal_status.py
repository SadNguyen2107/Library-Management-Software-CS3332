from src.extensions import db


class RenewalStatus(db.Model):
    __tablename__ = "RENEWAL_STATUS"

    status = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return (
            f"<RenewalStatus(status='{self.status}', description='{self.description}')>"
        )
