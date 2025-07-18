# Getting Started

This is the setup guide for minjee systems backend

## Environment

Use pythons venv command to create enviroment for isolation of packages

##### make virtual environment
```bash
python -m venv <name_of_environment> 
```
##### running virtual environment on linux or bash
```bash
source name_of_environment/Scripts/activate
```
##### running virtual environment on windows cmd or powershell
```cmd
name_of_environment\Scripts\activate
```
###### note: when running directory commands in cmd use "\" instead of "/"

## Python packages
###### note: run this commands with the virtual environment enables as per instructions above.

run 
```bash
pip install -r requirements.txt
```
or
```bash
python -m pip install -r requirements.txt
```
or 
```bash
uv add -r requirements.txt
```
## Migrations / Database setup
 Alembic is used to manage database migrations with versioning. The database tables are defined on models directory along with all the schemas that will be used for managing data flows in the backend. The database connections is defined at config directoy under env module. 

###### note: env.py module would be hidden as this would be our .env file configuration because that would be easier to implement than adding another package.

##### run migrations revision 
```bash
alembic revision --autogenerate -m "message for what changes in the database or something"
```
###### note: revision is for when there are changes made in models module in models direcotry. DO NOT RUN THIS EVERYTIME!!!!!

##### run migrations
```bash
alembic upgrade head
```
this will run the migrations on the latest revision and make the database tables and make sure that the database is set up correctly before hand.
##### run migrations to previous version 
```bash
alembic downgrade head
```
this will run the migrations in which would drop the changes made from the upgrade command.
###### note: you can see the changes from the commands at migrations/versions directory


# DOCS
/api/v1/docs -- main public docs 
