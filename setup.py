# -*- coding: utf-8 -*-
# https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

#from distutils.core import setup
from setuptools import setup

setup(name='nanoqtt',
      version='0.0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Jaime Saez',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['nanoqtt'],
      zip_safe=False)