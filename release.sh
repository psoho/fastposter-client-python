#!/bin/bash

# 发布到 https://pypi.org/

function build() {
  python setup.py sdist && python setup.py bdist_wheel
}

function push() {
  twine upload dist/* && rm -rf dist/*
}


function buildAndPush() {
    python setup.py sdist && python setup.py bdist_wheel && push
}


buildAndPush