#!/bin/bash

# Import global variables
source ./scripts/global_var.sh

# Activate python virtual environment
source "$PYTHON_VIR_ENV_DIR/bin/activate"

# Run Flask
export FLASK_APP=api.py
export FLASK_DEBUG=1
python3 -m flask run

# Deactivate python virtual environment when test is finished
deactivate
