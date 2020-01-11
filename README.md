# Atlas

Generating testing data is always a pain. Atlas provides a queryable, RESTful API that returns random, geolocatable addresses in the United States.

## Install
Atlas is designed to be run using Docker, though it can be installed and run locally. In either case, the following environmental variables are available and are provided with their default values.

- pg_user [postgres]
- pg_pw [psql]
- pg_host [localhost]
- pg_port [5432]
- regions ['northeast,west,south,midwest]

#### Docker
The recommended install and run method. Included in ./Deployment is a docker-compose.yml file that can be used to run the application directly with the database. For use with an existing PostgreSQL datbase, 