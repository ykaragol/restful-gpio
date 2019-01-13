# A hack to not break on systems other than Raspberry Pi
# See: https://github.com/RPi-Distro/python-gpiozero/issues/600#issuecomment-428439002 for details
import os
os.environ['GPIOZERO_PIN_FACTORY'] = os.environ.get('GPIOZERO_PIN_FACTORY', 'mock')

from gpiozero import LED

leds = {}

class GPIOManager():
	def set_state(self, port, state):
		if port not in leds:
			leds[port] = LED(int(port))

		led = leds[port]
		if state=="on":
			led.on()
		else:
			led.off()

		return 201

	def get_state(self, port):
		# TODO ...
		pass

import atexit

def cleanup():
	for port, led in leds.items():
		led.close()
		print("closed LED for port:", port)

atexit.register(cleanup)
