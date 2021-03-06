from flask_restful import Resource, reqparse

class RaspberryIOController(Resource):
	def __init__(self, **kwargs):
		self.gpio_manager = kwargs['gpio_manager']


	def put(self, port):
		# TODO can we use parser globally thread-safe?
		parser = reqparse.RequestParser()
		parser.add_argument("state")
		args = parser.parse_args()

		self.gpio_manager.set_state(port, args["state"])

		return {'state': args["state"], 'port': port}

	def get(self, port):
		state = self.gpio_manager.get_state(port)

		return {'state': state, 'port': port}
