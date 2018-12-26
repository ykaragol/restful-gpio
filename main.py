from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

from gpio import GPIOController
api.add_resource(GPIOController.GPIO, '/gpio/<string:pin_id>')

if __name__ == '__main__':
    app.run(debug=True)

