#!/usr/bin/env python
from io import open
from setuptools import setup, find_packages
setup(
    name='fastposter-cloud-client',
    version='1.0.0',
    description='a package for fastposter cloud client',
    long_description='fastposter-cloud python客户端，轻松开发海报。',
    author='Alex',
    author_email='service@fastposter.net',
    license='Apache License 2.0',
    url='https://github.com/psoho/fastposter-cloud-client-python',
    download_url='https://github.com/psoho/fastposter-cloud-client-python/main.zip',
    packages=find_packages(),
    install_requires=['requests==2.28.2']
)
