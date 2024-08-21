from datetime import datetime, timedelta

from flask import json, Response
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from src.extensions import db, mail

from src.models.user import User
from src.models.book_copy import BookCopy
from src.models.deposit import Deposit

from src.user.service.validation import (
    validate_hust_id,
    validate_phone_number,
    validate_email_address,
    validate_password,
)

from otp import (
    generate_otp,
    verify_otp,
)


def create_a_user(data):
    # Extract data from the request
    user_id = data.get('id')  # Assuming `id` is provided and manually set
    name = data.get('name')
    phone_number = data.get('phone_number', None)  # Default to None if not provided
    if phone_number == "":
        phone_number = None
        
    email_address = data.get('email_address')
    password = data.get('password')  # Assuming you'll handle password hashing

    user_id_as_str = str(user_id)
    
    # Validate ID
    result, status_code = validate_hust_id(user_id_as_str)
    if status_code == 400:
        return result, status_code
    
    # Validate phone_number
    result, status_code = validate_phone_number(phone_number)
    if status_code == 400:
        return result, status_code
    
    # Validate Email Address
    result, status_code = validate_email_address(email_address, name, user_id_as_str)
    if status_code == 400:
        return result, status_code
    
    # Validate Password
    result, status_code = validate_password(password)
    if status_code == 400:
        return result, status_code

    # Check for unique constraints
    if user_id and User.query.filter_by(id=user_id).first():
        return {
            "message": "ID already exists."
        }, 400
    
    if phone_number and User.query.filter_by(phone_number=phone_number).first():
        return {
            "message": "Phone number already in use."
        }, 400
    
    if User.query.filter_by(email_address=email_address).first():
        return {
            "message": "Email address already in use."
        }, 400
        
    
    # Assign system values
    membership_type = 'Public'  # Default system value
    user_role = 'Member'  # Default system value
    account_status = 'Active'  # Default system value

    # Create a new User object
    new_user = User(
        id=user_id,
        name=name,
        phone_number=phone_number,
        email_address=email_address,
        membership_type=membership_type,
        user_role=user_role,
        account_status=account_status,
        password=generate_password_hash(password)  # Store hashed password
    )

     # Add the new user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        # Handle unexpected errors
        return {
            "message": e
        }, 500


    return {
        "message": "User created successfully",
    }, 201


def borrow_a_book(user_id: int, data: dict):
    """
    Process the borrowing of a book by a user.

    :param user_id: ID of the user borrowing the book
    :param data: Data containing the book_id and other necessary info
    :return: Success message or error message
    """
    User.query.filter_by(id=user_id) \
        .first_or_404("User not found.")

    book_copy = BookCopy.query.filter_by(id=data['book_copy_id']) \
        .first_or_404("Book copy not found.")


    if book_copy.book_status != 'Available':
        return {
            "message": "Book is not available for borrowing."
        }, 400

    # Calculate due date
    issue_date = datetime.utcnow().date()
    due_date = issue_date + timedelta(days=14)  # Assuming a 2-week borrowing period

    # Create a new deposit entry
    new_deposit = Deposit(
        borrower_id=user_id,
        book_id=book_copy.id,
        issue_date=issue_date,
        due_date=due_date,
    )

    # Update book copy status to 'Borrowed'
    book_copy.book_status = 'Borrowed'

    # Save to database
    db.session.add(new_deposit)
    db.session.commit()

    return {"message": "Book borrowed successfully."}, 201


def login_a_user(data: dict):
    """
    Authenticate a user with email and password.

    :param data: A dictionary containing 'email' and 'password'
    :return: A success message or error message with appropriate HTTP status code
    """
    email = data.get('email')
    password = data.get('password')

    # Check if the user exists
    user = User.query.filter_by(email_address=email) \
        .first_or_404("User not found.")
        
    # Validate password
    if not check_password_hash(user.password, password):
        return {"message": "Invalid password."}, 401

    # Log the user in (this creates a session)
    login_user(user)
    
    return {
        "message": "Login successful.",
        "user_id": user.id,
    }, 200
    
    
def send_otp_code_to_mail(data: dict):
    user_id = data.get('user_id', None)
    user_email = data.get('email', None)


    # Check for the user_id 
    user_by_id = User.query.filter_by(id=user_id) \
        .first_or_404("User did not have an account yet!")
    
    # Check for the user_email
    user_by_mail = User.query.filter_by(email_address=user_email) \
        .first_or_404("User did not have an account yet!")
    
    
    # Check user_id with user_email
    if user_by_id.id != user_by_mail.id:
        return {
            'status': 'failure',
            'message': 'user_id did not match with user_email'
        }, 400
    

    # Get the OTP code
    otp_code = generate_otp(user_id=user_id)

    # Send mail to the user
    mail.send_mail_to(
        mail_from="nguyentrungson217@gmail.com",
        mail_to=user_email,
        mail_subject="Forgot Password ???",
        plain_message="",
        html_message=f"""
            <h1>Here is the OTP Code to recover</h1>
            <pre><code>{otp_code}</code></pre>
        """,
        image_directory="images/forgot_password.jpg",
    )
    
    
    return {
        'message': f"Send OTP code successfully to {user_email}. Check your Junk Mail."
    }, 200
    


def check_otp_and_login(data: dict):
    user_id = data.get('user_id', None)
    user_email = data.get('email', None)
    otp_code = data.get('otp_code', None)
    
    # Check for the user_id 
    user_by_id = User.query.filter_by(id=user_id) \
        .first_or_404("User did not have an account yet!")
    
    # Check for the user_email
    user_by_mail = User.query.filter_by(email_address=user_email) \
        .first_or_404("User did not have an account yet!")
    
    
    # Check user_id with user_email
    if user_by_id.id != user_by_mail.id:
        return {
            'status': 'failure',
            'message': 'user_id did not match with user_email'
        }, 400
    
    if verify_otp(user_id=user_id, otp_code=otp_code):
        # If Success
        # Log the user in (this creates a session)
        login_user(user_by_id)
        
        return {
            'status': 'success',
            'message': 'You have login make sure to update your password :D',
            'user_id': user_id,
        }, 200
        
    return {
        'status': 'failure',
        'message': 'Incorrect OTP code',
    }, 400