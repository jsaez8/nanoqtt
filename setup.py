# -*- coding: utf-8 -*-
# https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

#from distutils.core import setup
from setuptools import setup

setup(name='nanoqtt',
      version='0.0.1',
      description='Extension of qtt and qcodes for Nanoelectronics group',
      url='https://github.com/nanoelectronics-new',
      license='MIT',
      packages=['nanoqtt'],
      zip_safe=False)