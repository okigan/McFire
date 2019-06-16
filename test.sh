#!/usr/bin/env bash

jupytext --test --to ipynb  mcfire/mcfire.py
jupytext --to ipynb  mcfire/mcfire.py
pycodestyle -v --exclude=*.pynb_checkpoints/* mcfire
py.test -v

