# coding=utf-8

from setuptools import setup, find_packages

setup(name="notes",
      version="0.1.0",
      options={},
      description="Simple note taking utility",
      author="carlba",
      packages=find_packages(),
      install_requires=['click'],
      entry_points={
          'console_scripts': [
              'notes = notes.cli:main'
          ]
      }
      )
