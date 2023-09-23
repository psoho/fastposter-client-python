#!/usr/bin/env python
from io import open
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fastposter',
    version="1.6.1",
    description='A Python client for fastposter cloud',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alex',
    author_email='service@fastposter.net',
    license='MIT License (MIT)',
    url='https://github.com/psoho/fastposter-client-python',
    # download_url='',
    packages=find_packages(),
    install_requires=['requests==2.31.0'],
    project_urls={
        "Documentation": "https://fastposter.net/doc/sdk/python.html",
        "Source": "https://github.com/psoho/fastposter-client-python",
    },
)
