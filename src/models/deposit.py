from src.extensions import db


class Deposit(db.Model):
    __tablename__ = "DEPOSIT"
    
    borrower_id = db.Column(
        db.Integer, 
        db.ForeignKey("USER.id"), 
        primary_key=True, 
        nullable=False,
    )
    book_id = db.Column(
        db.Integer,
        db.ForeignKey("BOOK_COPY.id"),
        primary_key=True,
        nullable=False,
    )
    issue_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    overdue_fines = db.Column(db.Integer, default=0)
    renewal_status = db.Column(
        db.String(10),
        db.ForeignKey("RENEWAL_STATUS.status"),
        default="First-time",
    )

    def __repr__(self):
        return f"<Deposit(borrower_id={self.borrower_id}, book_id={self.book_id}, issue_date={self.issue_date}, due_date={self.due_date}, return_date={self.return_date}, overdue_fines={self.overdue_fines}, renewal_status='{self.renewal_status}')>"
