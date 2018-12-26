import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
name="restful-gpio",
version="0.1.0",
license="MIT",
author="ykaragol",
python_requires='>3.4.0',
packages=["gpio"],
install_requires=required
)

