# Bloom Challenge Instructions

# 1. Create Postgres & Postgreql user

Assuming you are running a postgres server locally

```
export PATH=/Applications/Postgres.app/Contents/Versions/latest/bin/:$PATH

createdb -U postgres -h localhost -p 5432 -d bloom

createuser postgres -h localhost -d bloom

psql -d bloom -U postgres -h localhost -p 5432
```
