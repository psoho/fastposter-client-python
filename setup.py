#!/usr/bin/env python
from io import open
from setuptools import setup, find_packages
from fastposter.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fastposter',
    version=__version__,
    description='A Python client for fastposter cloud',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alex小新',
    author_email='service@fastposter.net',
    license='MIT License (MIT)',
    url='https://github.com/psoho/fastposter-cloud-client-python',
    # download_url='',
    packages=find_packages(),
    install_requires=['requests==2.28.2'],
    project_urls={
        "Documentation": "https://cloud.fastposter.net/doc/guide/",
        "Source": "https://github.com/psoho/fastposter-cloud-client-python",
    },
)
