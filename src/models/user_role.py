from src.extensions import db


# USER_ROLE Model
class UserRole(db.Model):
    __tablename__ = 'user_role'
    role = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<UserRole(role='{self.role}', description='{self.description}')>"
