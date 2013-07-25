#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(
		name='python-emotiv',
		version='0.1',
		author='Sebastian Imlay',
		packages=['emotiv'],
		provides=['xp_board'],
		#data_files=[('/etc/udev/rules.d', ['udev/99-emotiv-epoc.rules'])],
		#scripts
		url='http://github.com/simlay/python-emotiv',
		description='Python library to access Emotiv EPOC EEG headset data',
)
