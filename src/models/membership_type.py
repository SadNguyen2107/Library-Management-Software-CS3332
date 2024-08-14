from src.extensions import db


class MembershipType(db.Model):
    __tablename__ = "MEMBERSHIP_TYPE"

    type = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<MembershipType(type='{self.type}', description='{self.description}')>"
