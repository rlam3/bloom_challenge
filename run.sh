export FLASK_APP=run_api.py
export FLASK_DEBUG=TRUE
export FLASK_ENV=development
export PYTHONPATH="${PYTHONPATH}:${pwd}"
flask run
