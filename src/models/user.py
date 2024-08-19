from src.extensions import db


# USER Model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, default='None')
    phone_number = db.Column(db.String, nullable=False, unique=True)
    email_address = db.Column(db.String, nullable=False, unique=True)
    membership_type = db.Column(db.String(50), db.ForeignKey('membership_type.type', onupdate="CASCADE", ondelete="SET NULL"), default='Public')
    user_role = db.Column(db.String(50), db.ForeignKey('user_role.role', onupdate="CASCADE", ondelete="SET NULL"), default='Member')
    account_status = db.Column(db.String(50), default='Active')
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email_address='{self.email_address}', membership_type='{self.membership_type}', user_role='{self.user_role}', account_status='{self.account_status}')>"
