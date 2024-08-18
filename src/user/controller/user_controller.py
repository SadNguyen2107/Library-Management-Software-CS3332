from flask import request
from flask_restx import Resource

from src.user.util.dto import UserDto
from src.user.service.GET import (
    get_all_users,
    get_a_user,
    get_borrowed_history,
)
from src.user.service.POST import (
    create_a_user,
    borrow_a_book
) 
from src.user.service.PUT import (
    update_a_user,
)

api = UserDto.api
_user_dto = UserDto.user_dto


@api.route('/users')
class UserList(Resource):

    @api.doc('List all available users')
    @api.marshal_list_with(_user_dto, envelope='users')
    def get(self):
        """List all the available users"""
        return get_all_users()


@api.route('/user')
class User(Resource):
    
    @api.doc("Create a new user")
    @api.expect(_user_dto, validate=True)
    def put(self):
        """Create a new user profile"""
        data = request.json
        return create_a_user(data)
    
        
@api.route('/user/<int:user_id>')
@api.param('user_id', "The User Identifier", type=int)
class User(Resource):

    @api.doc("Get a user")
    @api.marshal_with(_user_dto)
    def get(self, user_id):
        """Get a user given its ID"""
        return get_a_user(user_id=user_id)
    
    
    @api.doc("Update a user")
    @api.expect(_user_dto, validate=True)
    def put(self, user_id):
        """Update a user given its ID"""
        data = request.json
        return update_a_user(user_id=user_id, new_data=data)
    


@api.route('/user/<int:user_id>/borrow_history')
@api.param('user_id', "The User Identifier", type=int)
class UserBorrowHistory(Resource):

    @api.doc("Get user borrowed history.")
    def get(self, user_id):
        """Get all book borrowed by user"""
        return get_borrowed_history(user_id=user_id)
    


@api.route('/user/<int:user_id>/borrow')
@api.param('user_id', "The User Identifier", type=int)
class UserBorrow(Resource):

    @api.doc("Allow user to borrow a book.")
    def post(self, user_id):
        """Allow user to borrow a book"""
        data = request.json
        return borrow_a_book(user_id=user_id, data=data)