#!/bin/bash

# Import global variables
source scripts/global_var.sh

if [ -d "$VIR_ENV_DIR" ]; then
    rm -r "$VIR_ENV_DIR"
    echo -e "\nRemoved python virtual environment.\n"
else
    echo -e "\nPython virtual environment is already cleaned up!\n"
fi
