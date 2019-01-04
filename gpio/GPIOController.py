from flask_restful import Resource,reqparse
from gpio import GPIOManager

class GPIO(Resource):
	def put(self, port):
		parser = reqparse.RequestParser()
		parser.add_argument("status")
		args = parser.parse_args()

		GPIOManager.set_state(port, args["status"])

		return 201
