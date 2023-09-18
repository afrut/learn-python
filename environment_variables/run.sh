#!/bin/bash
# A script that sources a file and makes every variable an environment variable.
# Useful for loading configs into python as environment variables.
set -a
source env_vars
set +a
python main.py