#!/bin/bash
# Basics of using the Python code formatter black
rm test_black_formatted.py
cp test_black_raw.py test_black_formatted.py
black test_black_formatted.py