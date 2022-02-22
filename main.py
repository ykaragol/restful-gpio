from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# IO Manager:
from gpio.GPIOManager import GPIOManager
gpioManager = GPIOManager()

# Rest Controller
from raspberryio.controller import RaspberryIOController

# define url mappings
api.add_resource(RaspberryIOController, '/gpio/<string:port>', resource_class_kwargs={ 'gpio_manager': gpioManager })

# for UI mapping:
from flask import render_template
@app.route('/')
def hello_world():
    return render_template('hello.html')

# To run app:
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) # Never ever use in debug mode at prod!
