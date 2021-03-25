# -*- coding: utf-8 -*-
# https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html

from distutils.core import setup
#from setuptools import setup

setup(name='qtt_extension',
      version='0.0.1',
      description='Extension of qtt library',
      url='https://github.com/jsaez8/qcodes_qtt_extension',
      license='MIT',
      packages=['qtt_extension'],
      zip_safe=False)