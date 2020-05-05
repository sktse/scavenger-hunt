#!/usr/bin/env bash

# Create a virtual environment and install python dependencies

if [ -d "venv" ]; then
    echo "Not creating a virtual environment; one already exists."
else
    python3 -m venv venv
fi

if [ -z "$CI" ]; then
    # Turn on the virtual environment
    source venv/bin/activate
fi

if [ ! -d "venv" ]; then
    touch requirements.txt
fi

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
