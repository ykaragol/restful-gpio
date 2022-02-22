# restful-gpio

Provides REST support for raspberry I/O manager.

A REST wrapper for [python-gpiozero](https://github.com/RPi-Distro/python-gpiozero) library.


## Dependencies:
- flask-restful for rest support
- gpiozero for io support of raspberry

## How to run
- Run `python3 setup.py install`
- Run `python3 main.py`
- Application will be served at `http://localhost:5000` 

## How to test 

- Run `python3 setup.py install`
- Run `python3 tests/test_raspberryio.py`
