#!/usr/bin/env python
from setuptools import setup, find_packages
import subprocess
import os
import sys

__doc__ = """
App for Django featuring class based email sending
"""


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'Django>=1.6',
    'markdown',
]

if sys.version.startswith("2.6"):
    install_requires.append("importlib")

STAGE = 'alpha'

version = (1, 0, 0, STAGE)


def get_version():
    number = '.'.join(map(str, version[:3]))
    stage = version[3]
    if stage == 'final':
        return number
    elif stage == 'alpha':
        process = subprocess.Popen('git rev-parse HEAD'.split(), stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return number + '-' + str(stdout.strip())[:8]

setup(
    name='django-emailtools-reloaded',
    version=get_version(),
    description=__doc__,
    long_description=read('README.rst'),
    packages=[package for package in find_packages() if package.startswith('emailtools')],
    url="https://github.com/barseghyanartur/django-emailtools-reloaded",
    author="Artur Barseghyan",
    author_email='artur.barseghyan@gmail.com',
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
)
