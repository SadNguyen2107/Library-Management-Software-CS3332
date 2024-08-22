from flask import request
from flask_restx import Resource
from flask_login import (
    login_required,
    logout_user,
)
from src.authorization import (
    librarian_required,
    own_profile_or_librarian_required,
)

from src.user.util.dto import UserDto
from src.user.service.GET import (
    get_all_users,
    get_a_user,
    get_borrowed_history,
)
from src.user.service.POST import (
    create_a_user,
    borrow_a_book,
    process_book_return,
    login_a_user,
    send_otp_code_to_mail,
    check_otp_and_login,
) 
from src.user.service.PUT import (
    update_a_user,
    update_member_account_status,
)

api = UserDto.api
_user_dto = UserDto.user_dto
_user_register_dto = UserDto.user_register_dto
_user_detail_dto = UserDto.user_detail_dto
_user_update_dto = UserDto._user_update_dto
_borrow_history_dto = UserDto.borrow_history_dto
_book_request_dto = UserDto.borrow_request_dto
_login_dto = UserDto.login_dto
_user_email_dto = UserDto.user_email_dto
_otp_dto = UserDto.otp_dto
_return_book_request_dto = UserDto.return_book_request_dto
_account_status_update_dto = UserDto.account_status_update_dto


@api.route('/users')
class UserList(Resource):

    @api.doc('List all available users with pagination')
    @login_required
    @librarian_required
    @api.param("page", "The current page", default=1, type=int)
    @api.param("per_page", "The maximum number of items on a page", default=5, type=int)
    @api.marshal_list_with(_user_dto, envelope='users')
    def get(self):
        """List all the available users with pagination"""
        # Get the page number and the number of items per page from the query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        return get_all_users(page, per_page)


@api.route('/user')
class User(Resource):
    
    @api.doc("Create a new user")
    @api.response(201, "User created successfully")
    @api.expect(_user_register_dto, validate=True)
    def post(self):
        """Create a new user profile"""
        data = request.json
        return create_a_user(data)
    


@api.route('/user/<int:user_id>')
@api.param('user_id', "The User Identifier", type=int)
class User(Resource):

    @api.doc("Get a user")
    @login_required
    @own_profile_or_librarian_required
    @api.response(404, "User not found.")
    @api.marshal_with(_user_detail_dto)
    def get(self, user_id):
        """Get a user given its ID"""
        return get_a_user(user_id=user_id)


@api.route('/user/<int:user_id>/update')
@api.param('user_id', "The User Identifier", type=int)
class UpdateInfo(Resource):

    @api.doc("Update a user")
    @login_required
    @own_profile_or_librarian_required
    @api.expect(_user_update_dto, validate=True)
    def put(self, user_id):
        """Update a user given its ID"""
        data = request.json
        return update_a_user(user_id=user_id, new_data=data)
    
    
@api.route('/user/login')
class Login(Resource):
    
    @api.doc("Login into existed account.")
    @api.expect(_login_dto, validate=True)
    def post(self):
        """Login into existed account"""
        data = request.json
        return login_a_user(data)

    
@api.route('/user/<int:user_id>/logout')
@api.param('user_id', "The User Identifier", type=int)
class Logout(Resource):

    @api.doc("Logout from the current session.")
    @login_required
    def post(self, user_id):
        """Logout the current user"""
        logout_user()
        return {"message": "Logout successful."}, 200



@api.route('/user/<int:user_id>/borrow_history')
@api.param('user_id', "The User Identifier", type=int)
class UserBorrowHistory(Resource):

    @api.doc("Get user borrowed history.")
    @login_required
    @own_profile_or_librarian_required
    @api.marshal_list_with(_borrow_history_dto, envelope='history')
    def get(self, user_id):
        """Get all book borrowed by user"""
        return get_borrowed_history(user_id=user_id)
    


@api.route('/user/<int:user_id>/borrow')
@api.param('user_id', "The User Identifier", type=int)
class UserBorrow(Resource):

    @api.doc("Allow user to borrow a book.")
    @login_required
    @own_profile_or_librarian_required
    @api.expect(_book_request_dto, validate=True)
    def post(self, user_id):
        """Allow user to borrow a book"""
        data = request.json
        return borrow_a_book(user_id=user_id, data=data)


@api.route('/user/forgot_password')
class UserForgotPassword(Resource):

    @api.doc("If the user forgot their password -> Send a OTP")
    @api.expect(_user_email_dto, validate=True)
    def post(self):
        """Allow user to retrieve their password by sending a OTP code to their mail"""
        data = request.json
        return send_otp_code_to_mail(data)
    

@api.route('/user/verify_otp_code')
class VerifyOtpCode(Resource):

    @api.doc("Verify the OTP code from the user")
    @api.response(200, "Successfully login into the account, remember to update your password")
    @api.response(400, "Incorrect OTP code")
    @api.expect(_otp_dto, validate=True)
    def post(self):
        """Verify the OTP code given by the user"""
        data = request.json
        return check_otp_and_login(data)
    
    
@api.route('/user/<int:user_id>/return_book')
@api.param('user_id', "The User Identifier", type=int)
class UserReturnBook(Resource):

    @api.doc("User return book to the librarian.")
    @login_required
    @own_profile_or_librarian_required
    @api.expect(_return_book_request_dto, validate=True)
    def post(self, user_id):
        """User return book to the librarian"""
        data = request.json
        return process_book_return(user_id=user_id, data=data)
    
    
@api.route('/librarian/update_member_account_status')
class UpdateAccountStatus(Resource):

    @api.doc("Update the account status of a user.")
    @login_required
    @librarian_required
    @api.response(200, "Member account_status updated complete")
    @api.response(404, "Member not found.")
    @api.expect(_account_status_update_dto, validate=True)
    def put(self):
        """Update the account status of a user.
           
           2 options only:  'Active' or 'Inactive'
        """
        data = request.json
        return update_member_account_status(data=data)