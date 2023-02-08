#!/usr/bin/env python
from io import open
from setuptools import setup, find_packages
from fastposter.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fastposter',
    version=__version__,
    description='a package for fastposter cloud client',
    long_description=long_description,
    author='Alex',
    author_email='service@fastposter.net',
    license='MIT License',
    url='https://github.com/psoho/fastposter-cloud-client-python',
    download_url='https://github.com/psoho/fastposter-cloud-client-python/main.zip',
    packages=find_packages(),
    install_requires=['requests==2.28.2']
)
