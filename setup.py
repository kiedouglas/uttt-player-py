#!/usr/bin/env python3

from setuptools import setup

setup(name='ultimate_ttt_player',
      version='0.1',
      description='Sample player implementations for UTTT games',
      author='socialgorithm'
      url='https://github.com/socialgorithm/uttt-player-py',
      packages=['ultimate_ttt_player'],
	  setup_requires=['ultimate_ttt','pytest-runner'],
	  tests_require=['ultimate_ttt','pytest']
     )
