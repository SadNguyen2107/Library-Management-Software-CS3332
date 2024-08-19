from src.extensions import db


# MEMBERSHIP_TYPE Model
class MembershipType(db.Model):
    __tablename__ = 'membership_type'
    type = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<MembershipType(type='{self.type}', description='{self.description}')>"
