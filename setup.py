"""Setup.py for installation purposes."""

from setuptools import setup

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='puppy-example-app',
    description='PuPPy API',
    author='Chelsea Dole',
    author_email='chelseadole@gmail.com',
    url='http://chelseadole.com',
    include_package_data=True,
    install_requires=required_packages,
)
