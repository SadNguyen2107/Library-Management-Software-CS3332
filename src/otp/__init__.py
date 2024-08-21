import pyotp
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError


from src.extensions import db
from src.models.otp import OTP


def cleanup_expired_otps(expiry_duration: int):
    """
    Cleanup expired OTP records.

    Args:
    expiry_duration (int): The expiry duration of OTP in seconds.
    """
    cutoff_time = datetime.utcnow() - timedelta(seconds=expiry_duration)
    OTP.query.filter(OTP.created_at < cutoff_time).delete()
    db.session.commit()


def generate_otp(user_id: int) -> str:
    """
    Generate an OTP code for a given user_id and handle expiry of old OTP records.

    Args:
    user_id (int): The user ID for whom to generate the OTP.

    Returns:
    str: The generated OTP code.
    """
    # Generate a new OTP code
    otp = pyotp.TOTP(pyotp.random_base32())
    otp_code = otp.now()
    
    # Define the OTP expiry duration
    expiry_duration = 300  # OTP expiry in seconds

    try:
        # Cleanup expired OTPs first
        cleanup_expired_otps(expiry_duration)
        
        # Check if an OTP record already exists for the given user_id
        existing_otp = OTP.query.filter_by(user_id=user_id).first()
        
        if existing_otp:
            # Update the existing OTP record
            existing_otp.otp_code = otp_code
            existing_otp.created_at = datetime.utcnow()
            existing_otp.expires_in = expiry_duration
        else:
            # Create a new OTP record
            new_otp = OTP(
                user_id=user_id,
                otp_code=otp_code,
                created_at=datetime.utcnow(),
                expires_in=expiry_duration
            )
            db.session.add(new_otp)
        
        db.session.commit()
        
    except IntegrityError:
        db.session.rollback()  # Rollback the session in case of an error
        print("Error: Unable to insert or update OTP record")
    
    return otp_code


def verify_otp(user_id: int, otp_code: str):
    otp_entry = OTP.query.filter_by(user_id=user_id).first()
    if not otp_entry:
        return False
    if datetime.utcnow() - otp_entry.created_at > timedelta(seconds=otp_entry.expires_in):
        db.session.delete(otp_entry)
        db.session.commit()
        return False
    if otp_code == otp_entry.otp_code:
        db.session.delete(otp_entry)
        db.session.commit()
        return True
    return False