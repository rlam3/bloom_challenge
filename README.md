# Requirements

# 1. Split up the .dat file for easier sample size

To obtain first 100 lines:

```sh
head -100 test.dat > test100.dat
```

# How to start

```sh
poetry install
export PYTHONPATH="${PYTHONPATH}:${pwd}"
poetry shell # virtualenv with poetry

flask shell
```

# 1. Create Postgres & Postgreql user with Docker OR [https://postgresapp.com/](https://postgresapp.com/)

Assuming you are running a postgres server locally

```sh
docker run --name pgdb -p 5432:5432 --rm -e -e POSTGRES_DB="bloom" postgres

export PATH=/Applications/Postgres.app/Contents/Versions/latest/bin/:$PATH # get access to psql

createdb -h localhost -p 5432 -d bloom

psql -d bloom -h localhost -p 5432
```

# Parsing and play around with .dat file

```sh
flask shell
```

```py

from console import *

input_file = 'test10.dat'
csv_file_name = 'tes10t.csv'
super_man(input_file, csv_file_name, CreditTag, ConsumerTagScore, Consumer)

```

# Run API

```sh
export FLASK_APP=run_api.py
export FLASK_DEBUG=TRUE
export FLASK_ENV=development
export PYTHONPATH="${PYTHONPATH}:${pwd}"

flask db upgrade

flask run
```

---

# Approach

1. Split up sample size
2. Convert samller sample to csv for better parsing tests
3. Create ORM and migrate DB
4. Insert data with ORM
5. Load data from ORM to API
