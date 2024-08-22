from src.models.user import User
from src.models.book import Book
from src.models.deposit import Deposit
from src.models.book_copy import BookCopy

def get_all_users(page, per_page):
    # Return only the items in the current page
    paginated_users = User.query.paginate(
        page=page,
        per_page=per_page, 
        error_out=False,
    ).items  
    return paginated_users


def get_a_user(user_id: int):
    """
    Get a user by ID.

    :param user_id: ID of the user to retrieve
    :return: User data or error message
    """
    return User.query.filter_by(id=user_id).first_or_404("User not found.")    


def get_borrowed_history(user_id: int):
    """
    Get the borrowing history of a user.

    :param user_id: ID of the user whose borrowing history is to be retrieved
    :return: List of borrowed books or error message
    """
    user = User.query.filter_by(id=user_id) \
        .first_or_404("User not found.")
    
    
    borrow_history = Deposit.query \
        .join(BookCopy, Deposit.book_id == BookCopy.id) \
        .join(Book, BookCopy.isbn == Book.isbn) \
        .filter(Deposit.borrower_id == user_id) \
        .with_entities(BookCopy.id, Book.title, Deposit.issue_date, Deposit.due_date, Deposit.return_date, Deposit.overdue_fines, Deposit.renewal_status) \
        .all()
    
    if not borrow_history:
        return {"message": "No borrow history found for this user."}, 404
    
    # Format the response data
    history = [
        {
            "book_copy_id": record.id,
            "title": record.title,
            "issue_date": record.issue_date.strftime("%Y-%m-%d"),
            "due_date": record.due_date.strftime("%Y-%m-%d"),
            "return_date": record.return_date.strftime("%Y-%m-%d") if record.return_date else "Not returned",
            "overdue_fines": record.overdue_fines,
            "renewal_status": record.renewal_status,
        }
        for record in borrow_history
    ]
    
    return history, 200