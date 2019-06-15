#!/usr/bin/env bash

jupyter nbconvert --to python mcfire/mcfire.ipynb
pycodestyle -v mcfire
py.test -v