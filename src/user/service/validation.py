import re
from flask import Response


def validate_hust_id(hust_id: str) -> Response:
    # Validate ID
    id_pattern = re.compile(r'^(201[6-9]|2020|2021|2022|2023|2024)\d{4}$')
    if not id_pattern.match(hust_id):
        return {
            "message": "ID must be 8 digits: start with 4 digits between 2016 and 2024 and end with 4 digits."
        }, 400
        
    return {
        "message": "ID is valid."
    }, 200
        

def validate_phone_number(phone_number: str):
    if phone_number and (len(phone_number) != 10 or not phone_number.isdigit()):
        return {
            "message": "Phone number must be exactly 10 digits."
        }, 400

    return {
        "message": "Phone number is valid."
    }, 200

# Generate expected email address
def generate_expected_email(name: str, user_id: str):
    parts = name.split()

    if len(parts) == 2:
        last_name_initial = parts[1][0]
        other_initials = parts[0][0]
    else:
        last_name_initial = parts[-1]
        other_initials = ''.join([p[0] for p in parts[:-1]])

    email_prefix = f"{last_name_initial}.{other_initials}{user_id[2:]}"
    return f"{email_prefix}@sis.hust.edu.vn"
        

def validate_email_address(email_address: str, name: str, user_id: str):    
    if len(name.split()) < 2:
        return {
            "message": "Name must have at least two parts."
        }, 400

    expected_email = generate_expected_email(name, user_id)
    # Validate email_address based on the generated pattern
    if email_address != expected_email:
        return {
            "message": f"Email address must be {expected_email} for the provided name and ID."
        }, 400

    
    return {
        "message": "Email address is valid."
    }, 200

def validate_password(password):
    """
    Validate the password based on the following criteria:
    - At least 8 characters long
    - Contains at least 1 uppercase letter
    - Contains at least 1 lowercase letter
    - Contains at least 1 special character (e.g., !@#$%^&*())
    """
    if len(password) < 8:
        return {"message": "Password must be at least 8 characters long."}, 400

    if not re.search(r'[A-Z]', password):
        return {"message": "Password must contain at least 1 uppercase letter."}, 400

    if not re.search(r'[a-z]', password):
        return {"message": "Password must contain at least 1 lowercase letter."}, 400

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return {"message": "Password must contain at least 1 special character."}, 400

    return {"message": "Password is valid."}, 200