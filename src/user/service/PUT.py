from flask import json

from src.user.service.validation import (
    validate_phone_number,
    validate_password,
)
from src.extensions import db
from werkzeug.security import generate_password_hash

from src.models.user import User


def update_a_user(user_id: int, new_data: dict):
    """
    Update user information given its ID.

    :param user_id: ID of the user to update
    :param new_data: Dictionary containing the updated user information
    :return: Updated user data or error message
    """
    user = User.query.filter_by(id=user_id).first()
    
    if user is None:
        return {"message": "User not found."}, 404
    
    # Validate Phone_number
    if 'phone_number' in new_data:
        result, status_code = validate_phone_number(phone_number=new_data['phone_number'])
        if status_code == 400:
            return result, status_code
    
    # Validate Password
    if 'password' in new_data:
        result, status_code = validate_password(password=new_data['password'])
        if status_code == 400:
            return result, status_code

    # Update only allowed fields
    if 'address' in new_data:
        user.address = new_data.get('address', user.address)
    
    # Update user phone_number
    existing_user = User.query.filter_by(phone_number=new_data['phone_number']).first()
    if existing_user and existing_user.id != user_id:
        return {"message": "Phone number already exists."}, 400
    user.phone_number = new_data['phone_number']
    
    # Update User Password
    user.password = generate_password_hash(new_data['password'])
    
    # Commit changes to the database
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {"message": "An error occurred while updating the user."}, 500
    
    # Prepare the updated data to return
    updated_user_data = {
        'id': user.id,
        'name': user.name,
        'address': user.address,
        'phone_number': user.phone_number,
        'email_address': user.email_address,  # This remains unchanged
        'membership_type': user.membership_type,  # This remains unchanged
        'user_role': user.user_role,  # This remains unchanged
        'account_status': user.account_status,  # This remains unchanged
    }

    return updated_user_data, 200