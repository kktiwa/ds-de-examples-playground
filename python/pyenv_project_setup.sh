#!/usr/bin/env bash

TARGET_ENVIRONMENT_NAME=$1

pyenv virtualenv 3.9.9 "$TARGET_ENVIRONMENT_NAME"
pyenv local "$TARGET_ENVIRONMENT_NAME"
pip install -r requirements.txt
