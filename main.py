from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

from gpio import GPIOManager
from raspberryio.controller import RaspberryIOController

api.add_resource(RaspberryIOController, '/gpio/<string:port>',
    resource_class_kwargs={ 'gpio_manager': GPIOManager() })

if __name__ == '__main__':
    app.run(debug=True)
