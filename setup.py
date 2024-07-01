import os
from setuptools import setup, find_packages

version = os.getenv('VERSION')

setup(
    name='internetbs-api',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
)
