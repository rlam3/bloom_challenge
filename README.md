# How to start

```
poetry install
export PYTHONPATH="${PYTHONPATH}:${pwd}
poetry shell

flask shell
```

# 1. Create Postgres & Postgreql user

Assuming you are running a postgres server locally

```
export PATH=/Applications/Postgres.app/Contents/Versions/latest/bin/:$PATH

createdb -U postgres -h localhost -p 5432 -d bloom

createuser postgres -h localhost -d bloom

psql -d bloom -U postgres -h localhost -p 5432
```

# Parsing and play around with .dat file

```

ipython -i console.py


```

# Run application

```
export FLASK_APP=run_api.py
export FLASK_DEBUG=TRUE
export FLASK_ENV=development
export PYTHONPATH="${PYTHONPATH}:${pwd}"
flask run

flask db init
flask db migrate
flask db upgrade
```
