#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
  name='insect',
  version='0.1.0',
  description='auto installs modules by importing them',
  author='Leonardo Rossetti',
  author_email='me@lrossetti.com',
  url='https://github.com/odra/insect',
  download_url='https://github.com/odra/insect/archive/master.zip',
  packages=find_packages(),
  keywords=['importlib', 'import', 'auto-import'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Plugins',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Software Development',
    'Topic :: Utilities'
  ]
)
