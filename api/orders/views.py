from flask_restx import Namespace, Resource

order_namespace = Namespace('orders',description="A Namespace for Orders")

@order_namespace.route("/orders")
class OrderGetCreate(Resource):
    def get(self):
        """
            Get all orders
        """
        pass

    def post(self):
        """
            Place an new Order
        """
        pass



@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):
    def get(self,id):
        """
            Retrieve specific Order by Id
        """
        pass

    def put(self,id):
        """
        update an order with id
        """
        pass
    def delete(self,id):
        """
        Delete order with id
        """
        pass



@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):    

    def get(self, user_id,order_id):
        """
        Get a user's specific order
    """
        pass


@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
    def get(self, user_id):
        """
        Get all orders by a specific user
        """
        pass

@order_namespace.route("/order/status/<int:order_id>")
class UpdateOrderStatus(Resource):
    def patch(self, order_id):
        """
            Update an order status
        """
        pass