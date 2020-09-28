#!/bin/bash

# Import global variables
source ./scripts/global_var.sh

# Activate python virtual environment
source "$PYTHON_VIR_ENV_DIR/bin/activate"

# Run tests
echo "Running all tests..."
python3 -m unittest tests/*-tests.py

# Deactivate python virtual environment when test is finished
deactivate
