## Table of Contents
1. [Dependencies](#dependencies)
2. [Run the proejct](#run-the-project)
3. [Components](#components)

_Refer to the variables in the .env file for <> variables_

## Depdendencies
 - Docker compose

## Run the project
To run the project, run `docker compose up` in the root.
Use `docker compose up --build` to rebuild the images.


A pgAdmin instance is available at localhost://<PGADMIN_LISTEN_PORT>
Use the following parameters to configure the connection:
- Username: <PGADMIN_DEFAULT_EMAIL>
- Password: <PGADMIN_DEFAULT_PASSWORD>

- DB Hostname: db
- DB Username: <ORACLE_USER>
- DB Password: <ORACLE_PASSWORD>

## Components
This project is composed of the following components:

- Frontend
- Backend
- Database
- PgAdmin


### Frontend
App: localhost:8080

## Backend
API: localhost:8081
Swagger: localhost:8081/docs


## Refs

The original ref:

https://github.com/tiangolo/full-stack-fastapi-postgresql

is no longer maintened.

The frontend has been taken from an updated fork:

https://github.com/pyb4430/full-stack-fastapi-postgresql




After running the oracle container, run a SSH shell and use the command `./setPassword password`
CLOUDBEAVER USERNAME: cbadmin
CLOUDBEAVER PASSWORD: root
