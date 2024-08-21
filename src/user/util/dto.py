from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user_dto = api.model('user', {
        'id': fields.Integer(description='User Identification'),
        'name': fields.String(description='Username'),
        'address': fields.String(description='User home address'),
        'phone_number': fields.String(description='User phone number'),
        'email_address': fields.String(description='User email address'),
        'membership_type': fields.String(description='User membership type'),
        'user_role': fields.String(description='User role'),
        'account_status': fields.String(desription='User account status'),
    })
    
    user_register_dto = api.model("user_register", {
        'id': fields.Integer(required=True, description='User Identification'),  # Primary Key
        'name': fields.String(required=True, description='Username'),
        'phone_number': fields.String(description='User phone number'),  # Optional
        'email_address': fields.String(required=True, description='User email address'),
        'password': fields.String(required=True, description='User password'),  # Added password field
    })
    
    
    user_detail_dto = api.model('user_detail', {
        'id': fields.Integer(required=True, description='User Identification'),
        'name': fields.String(required=True, description='Username'),
        'address': fields.String(description='User home address'),
        'phone_number': fields.String(description='User phone number'),
        'email_address': fields.String(required=True, description='User email address'),
        'membership_type': fields.String(readonly=True, description='User membership type'),
        'user_role': fields.String(readonly=True, description='User role'),
        'account_status': fields.String(readonly=True, description='User account status'),
        'password': fields.String(required=True, description='User password'),
    })
    
    _user_update_dto = api.model('user_update', {
        'id': fields.Integer(readonly=True, description='User Identification'),
        'name': fields.String(readonly=True, description='Username'),
        'address': fields.String(description='User home address'),
        'phone_number': fields.String(description='User phone number'),
        'email_address': fields.String(readonly=True, description='User email address'),
        'membership_type': fields.String(readonly=True, description='User membership type'),
        'user_role': fields.String(readonly=True, description='User role'),
        'account_status': fields.String(readonly=True, description='User account status'),
        'password': fields.String(description='User password'),
    })
    
    
    borrow_history_dto = api.model('borrow_history', {
        'title': fields.String(readonly=True, description='Title of the borrowed book'),
        'issue_date': fields.String(readonly=True, description='Date when the book was issued (YYYY-MM-DD)'),
        'due_date': fields.String(readonly=True, description='Due date for returning the book (YYYY-MM-DD)'),
        'return_date': fields.String(readonly=True, description='Date when the book was returned (YYYY-MM-DD) or "Not returned" if not yet returned'),
        'overdue_fines': fields.Integer(readonly=True, description='Overdue fines for the book, if any'),
        'renewal_status': fields.String(readonly=True, description='Is user first-time borrow this book or renewed')
    })
    
    
    borrow_request_dto = api.model('borrow_request', {
        'book_copy_id': fields.Integer(required=True, description='Book Copy ID to be borrowed'),
    })
    
    login_dto = api.model('login', {
        'email': fields.String(required=True, description="User Hust Email"),
        'password': fields.String(required=True, description="User password")
    })
    
    user_email_dto = api.model('user_email', {
        'user_id': fields.Integer(required=True, description='User Identification'),
        'email': fields.String(required=True, description="User Hust Email"),
    })
    
    otp_dto = api.model('otp', {
        'user_id': fields.Integer(required=True, description='User Identification'),
        'email': fields.String(required=True, description="User Hust Email"),
        'otp_code': fields.String(required=True, description="User OTP"),
    })