
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'type': '2 ltr bottle', 'price': 125, 'qty': 250},
    'coke': {'type': '500 ml bottle', 'price': 45, 'qty': 500},
    'thumbs_up': {'type': '300 ml can', 'price': 60, 'qty': 250}
}

class Products(Resource):

    def get(self, product):
        return {product: products[product]}

api.add_resource(Products, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True)
