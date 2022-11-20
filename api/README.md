### Project Setup
* Requirements
  * Python 3.9
  * Postgres 14
  * Pipenv
  * PostGIS
* start a postgres server
* create a database with defaults for dev and add postgis
```
create database jailwatch;
create user jailwatch with encrypted password 'jailwatch123';
grant all privileges on database jailwatch to jailwatch;
\connect jailwatch;
CREATE EXTENSION postgis;
exit;
```
* set up python environment and start flask shell
```
pipenv install
pipenv shell
flask shell
```
* in the flask shell create the tables
```
from api.config import db
db.create_all()
exit()
```
* load in county and jail data
