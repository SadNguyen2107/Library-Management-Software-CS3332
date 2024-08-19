from datetime import date

from src.extensions import db
from src.models.renewal_status import RenewalStatus

# DEPOSIT Model
class Deposit(db.Model):
    __tablename__ = 'deposit'
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_copy.id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    issue_date = db.Column(db.Date, nullable=False, default=date.today)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    overdue_fines = db.Column(db.Integer, default=0)
    renewal_status = db.Column(db.String(50), db.ForeignKey('renewal_status.status', onupdate="CASCADE", ondelete="SET NULL"), default='First-time')

    # Ensure due_date is after issue_date
    __table_args__ = (
        db.CheckConstraint('due_date > issue_date', name='check_deposit_dates'),
    )

    def __repr__(self):
        return f"<Deposit(borrower_id={self.borrower_id}, book_id={self.book_id}, issue_date={self.issue_date}, due_date={self.due_date}, return_date={self.return_date}, overdue_fines={self.overdue_fines}, renewal_status='{self.renewal_status}')>"
