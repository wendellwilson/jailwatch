### Project Setup
* Requirements
  * Python 3.9
  * Postgres 14
  * Pipenv
* start a postgres server
* create a database defaults for dev
  * name = jailwatch
  * user = jailwatch
  * password = jailwatch123
* set up python environment and start flask shell
```
pipenv install
pipenv shell
flask shell
```
* in the flask shell create table
```
from api.config import db
db.create_all()
```

