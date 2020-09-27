#!/bin/bash

# Import global variables
source ./scripts/global_var.sh

# Activate the virtual environment of python
source "$PYTHON_VIR_ENV_DIR/bin/activate"

pip3 install Flask
pip3 install flask_cors

deactivate
