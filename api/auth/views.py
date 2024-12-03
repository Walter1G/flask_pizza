from flask_restx import Namespace, Resource

auth_namespace = Namespace('auth', description="A Namespace for authentication")

@auth_namespace.route("/")
class HelloAuth(Resource):
    def get(self):

        return {"message":"hello Auth"}