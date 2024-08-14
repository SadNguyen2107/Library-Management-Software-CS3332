from flask import request
from flask_restx import Resource

from src.user.util.dto import UserDto
from src.user.service.user_service import get_all_user

api = UserDto.api
_user_dto = UserDto.user_dto


@api.route('/users')
class UserList(Resource):

    @api.doc('list_of_available_users')
    @api.marshal_list_with(_user_dto, envelope='users')
    def get(self):
        """List all the available users"""
        return get_all_user()