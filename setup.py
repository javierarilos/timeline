#!/usr/bin/env python

from setuptools import setup

setup(name='timeline',
      version='0.2',
      description='Timeline calls your code back following a given time distribution (a planning).',
      author='Javier Arias',
      author_email='javier.arilos@gmail.com',
      url='https://github.com/javierarilos/timeline.git',
      packages=['timeline'],
      package_dir={'timeline': 'src/'},
      install_requires=[],
      scripts=[]
      )
