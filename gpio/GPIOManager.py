from gpiozero import LED

leds = {}

class GPIOManager():
	def set_state(port, state):
		if port not in leds:
			leds[port] = LED(int(port))

		led = leds[port]
		if state=="on":
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
		print("cleaned LED for port:", port)

atexit.register(cleanup)
