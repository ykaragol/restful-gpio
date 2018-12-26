from flask_restful import Resource,reqparse

from gpiozero import LED

leds = {}

class GPIO(Resource):
    def put(self, pin_id):
	parser = reqparse.RequestParser()
	parser.add_argument("status")
    	args = parser.parse_args()
        port = pin_id
        status = args["status"]

        if port not in leds:
            leds[port] = LED(int(port))

        led = leds[port]
    	if args["status"]=="on":
	    led.on()
    	else:
            led.off()

    	return 201


import atexit

def cleanup():
	for port, led in leds.items():
		led.close()
		del leds[port]
		del led	
		print "cleaned LED for port:", port

atexit.register(cleanup)
