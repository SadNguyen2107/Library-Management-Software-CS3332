from src.extensions import db


# RENEWAL_STATUS Model
class RenewalStatus(db.Model):
    __tablename__ = 'renewal_status'
    status = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return (
            f"<RenewalStatus(status='{self.status}', description='{self.description}')>"
        )
