from flask_restx import Namespace, Resource

order_namespace = Namespace('orders',description="A Namespace for Orders")

@order_namespace.route("/")
class OrderHello(Resource):
    def get(self):
        return {"message":"Hello from ,Orders"}