from flask_restx import Namespace, Resource, fields
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.users import User
from http import HTTPStatus

auth_namespace = Namespace('auth', description="A Namespace for authentication")

signup_model = auth_namespace.model(
    'SignUp', {
        'id':fields.Integer(description="user id"),
        'username':fields.String(required=True, description='a username'),
        'email':fields.String(required=True, description='an email'),
        'password':fields.String(required=True, description='user password')
    }
)

user_model=auth_namespace.model(
    'User',
    {
    'id':fields.Integer(description="user id"),
        'username':fields.String(required=True, description='a username'),
        'email':fields.String(required=True, description='an email'),
        'password':fields.String(required=True, description='user password'),
        'is_active':fields.Boolean(description='This shows that a user is active'),
        'is_staff':fields.Boolean(description='This shows if user is staff')
    }
)

@auth_namespace.route("/signup")
class SignUp(Resource):
    """
        Create a new user account
    """

    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):

        data = request.json
        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password')),

        )
        new_user.save()
        return new_user,HTTPStatus.CREATED


@auth_namespace.route('/login')
class LogIn(Resource):
    """ 
        Generate a JWT pair
    """
    def post(self):
        pass