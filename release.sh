#!/bin/bash

# https://pypi.org/

cd `dirname $0`
pwd

function build() {
  python3 setup.py sdist && python3 setup.py bdist_wheel
}

function push() {
  twine upload dist/* && rm -rf dist/*
}


function buildAndPush() {
    python3 setup.py sdist && python3 setup.py bdist_wheel && push
#    python3 setup.py sdist && push
}


buildAndPush
#build