from src.extensions import db


class UserRole(db.Model):
    __tablename__ = "USER_ROLE"

    role = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<UserRole(role='{self.role}', description='{self.description}')>"
