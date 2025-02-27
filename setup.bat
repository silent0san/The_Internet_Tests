#!/bin/bash

echo "Creating virtual environment"
python -m venv venv

echo "Activating virtual environment"
source venv/bin/activate

echo "Installing dependencies"
pip install -r requirements.txt

echo "Saving installed dependencies"
pip freeze > requirements.txt

echo "Setup complete. Virtual environment is ready to use"

echo "Running tests"
pytest