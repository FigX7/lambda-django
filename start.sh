#!/bin/sh
pipenv run python -m pip freeze > requirements.txt
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
/bin/sh