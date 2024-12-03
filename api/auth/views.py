from flask_restx import Namespace, Resource

auth_namespace = Namespace('auth', description="A Namespace for authentication")

@auth_namespace.route("/signup")
class SignUp(Resource):
    """
        Create a new user account
    """
    def post(self):
        pass


@auth_namespace.route('/login')
class LogIn(Resource):
    """ 
        Generate a JWT pair
    """
    def post(self):
        pass