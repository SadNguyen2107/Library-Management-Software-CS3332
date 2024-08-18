from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user_dto = api.model('user', {
        'id': fields.Integer(required=True, description='User Identification'),
        'name': fields.String(required=True, description='Username'),
        'phone_number': fields.String(required=True, description='User phone number'),
        'email_address': fields.String(required=True, description='User email address'),
        'membership_type': fields.String(required=True, description='User membership type'),
        'user_role': fields.String(required=True, description='User role'),
        'account_status': fields.String(required=True, desription='User account status'),
    })
    
    
    