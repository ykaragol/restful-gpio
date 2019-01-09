from raspberryio.controller import RaspberryIOController
import unittest

from flask import Flask
app = Flask(__name__)

class MockIOManager():
    def set_state(self, port, state):
        self.port = port
        self.state = state

class MyTest(unittest.TestCase):
    def test_put_method(self):
        mock = MockIOManager()
        controller = RaspberryIOController(gpio_manager = mock)
        with app.test_request_context('/dummy', data={'state': 'on'}):
            controller.put(12)
        self.assertEqual(mock.port, 12)
        self.assertEqual(mock.state, 'on')
