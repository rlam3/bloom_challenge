# Approach

1. Split up the .dat file for smaller sample size
2. Convert samller sample to csv for better parsing tests
3. Create database schema with tables using Flask-Migrate
4. Insert data with ORM and session commits
5. Load data from ORM to API

---

# Install Requirements

- [poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)
- postgres (docker or [https://postgresapp.com/](https://postgresapp.com/))
- [psql-cli](https://blog.timescale.com/tutorials/how-to-install-psql-on-mac-ubuntu-debian-windows/)

```sh
poetry install
export PYTHONPATH="${PYTHONPATH}:${pwd}"
poetry shell # virtualenv with poetry automatically

flask shell
```

---

## Create Postgres DB instance with Docker OR [MacOS Postgres.app](https://postgresapp.com/)

Assuming you are running a postgres server locally

```sh
docker run --name pgdb -p 5432:5432 --rm -e -e POSTGRES_DB="bloom" postgres

# Reference for psql-cli tool https://blog.timescale.com/tutorials/how-to-install-psql-on-mac-ubuntu-debian-windows/

# OR

# Ensure you have necessary postgersql cli tools
export PATH=/Applications/Postgres.app/Contents/Versions/latest/bin/:$PATH # get access to psql

createdb -h localhost -p 5432 -d bloom

psql -d bloom -h localhost -p 5432
```

## 1. Split up the .dat file for easier sample size

To obtain first 100 lines:

```sh
head -100 test.dat > test100.dat
```

## 3. Create database schema with tables using Flask-Migrate

```sh
❯ flask db upgrade
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 49e05cb5a29f, empty message
INFO  [alembic.runtime.migration] Running upgrade 49e05cb5a29f -> ec21a5e339db, empty message
```

## 4. Insert data with ORM and session commits

```py
❯ flask shell
Python 3.9.5 (default, May  4 2021, 03:33:11)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
IPython: 7.25.0
App: bloom_challenge.bloom_credit.factory [development]
Instance: /Users/raymondlam/Local Projects/instance
In [1]: from console import *
   ...:
   ...: input_file = 'test10.dat'
   ...: csv_file_name = 'tes10.csv'

In [2]: super_man(input_file, csv_file_name, CreditTag, ConsumerTagScore, Consumer)
```

Run the super_man function and it will take care of the rest.
remember to update the input and output filename of the test.dat file.

```py

from console import *

input_file = 'test100.dat'
csv_file_name = 'tes100.csv'

super_man(input_file, csv_file_name, CreditTag, ConsumerTagScore, Consumer) # <<<<<<< This is where the magic happens >>>>>>>
```

## 5. Load data from ORM to API

```sh
export FLASK_APP=run_api.py
export FLASK_DEBUG=TRUE
export FLASK_ENV=development
export PYTHONPATH="${PYTHONPATH}:${pwd}"

flask run
```

# Play with ORM

```py
❯ flask shell
Python 3.9.5 (default, May  4 2021, 03:33:11)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
IPython: 7.25.0
App: bloom_challenge.bloom_credit.factory [development]
Instance: /Users/raymondlam/Local Projects/instance
In [1]: cc = db.session.query(Consumer).all()

In [2]: c = cc[0]

In [3]: c
Out[3]: <Consumer: {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x10fb6ceb0>, 'ssn': 266667962, 'name': 'Norma Fisher', 'uuid': UUID('0a3d6ace-1216-4fed-a57b-78d80377e32b')}>

In [4]: c = Consumer.get_where(ssn='266667962')[0]

In [5]: c
Out[5]: <Consumer: {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x10fb6ceb0>, 'ssn': 266667962, 'name': 'Norma Fisher', 'uuid': UUID('0a3d6ace-1216-4fed-a57b-78d80377e32b')}>

In [6]: len(c.consumer_tag_scores.all())
Out[6]: 200
```
