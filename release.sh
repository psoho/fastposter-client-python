#!/bin/bash

# 发布到 https://pypi.org/

python setup.py sdist && python setup.py bdist_wheel && twine upload dist/* && rm -rf dist/*
