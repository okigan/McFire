#!/usr/bin/env bash

jupytext --test --to ipynb mcfire/mcfire.py
jupytext --to ipynb mcfire/mcfire.py
jupytext --test --to py:percent mcfire/mcfire.ipynb
pycodestyle -v --exclude=*.pynb_checkpoints/* mcfire
py.test -v

