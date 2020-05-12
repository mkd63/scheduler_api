# scheduler_api

## About
A server side API which functions for scheduler to schedule activities Built on django.

## Usage
To run the API locally:
1.	Setup a virtualenv and activate it.
2.	Install the packages as listed in the requirements.txt by running pip install. (Make sure you are in the virtual environment while doing this)
3.	The API uses some config variables to run in appropriate environments. Create a .env file and list the following variables:
  ```
  SECRET_KEY=DJANGO_GENERATED_SECRET_KEY
  DEBUG=True
  DATABASE_URL= postgres password
  ALLOWED_HOST=127.0.0.1
  ```
4.	Then finally, run python manage.py runserver to run the Django API server.

## PostgreSQL 
PostgreSQL relational database has been used to store and manage the data. 

### Setup
1.	Make sure you have Postgres installed and create a database named scheduler_development.
2.	Edit the DATABASE_URL in .env file and change it to your Postgres password.
3.	Go to your API directory and run python manage.py makemigrations to create the migration files for tables to created in the database from Django.
4.	Run python manage.py migrate to run the migration files and apply changes in PostgreSQL.


### Contributors

| Part           | Contributor                                   |
| :------------- | :-------------------------------------------- |
| Models and API | [Aahan Sharma](https://github.com/mkd63) |
| Postgres       | [Aahan Sharma](https://github.com/mkd63) |
