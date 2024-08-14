from src.extensions import db


class User(db.Model):
    __tablename__ = "USER"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, default="None")
    phone_number = db.Column(db.String, nullable=False, unique=True)
    email_address = db.Column(db.String, nullable=False, unique=True)
    membership_type = db.Column(
        db.String(10),
        db.ForeignKey("MEMBERSHIP_TYPE.type"),
        default="Public",
    )
    user_role = db.Column(
        db.String(10),
        db.ForeignKey("USER_ROLE.role"),
        default="Member",
    )
    account_status = db.Column(db.String(10), default="Active")
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email_address='{self.email_address}', membership_type='{self.membership_type}', user_role='{self.user_role}', account_status='{self.account_status}')>"
