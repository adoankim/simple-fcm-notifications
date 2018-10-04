#!/bin/bash

# create a virtual environment to isolate the dependencies
python -m venv virtual-environment 

# install the dependencies in the virtual environment
source ./virtual-environment/bin/activate
pip install -r requirements.txt