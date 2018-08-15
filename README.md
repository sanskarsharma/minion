
# minion - url shortener webapp

This is a utility app for minifying long urls. 
Demo is live on http://m96.pythonanywhere.com

## About project
- made using python Flask framework.
- Database used is MySQL, managed by SQLAlchemy

## Prerequisites for setup
Python3 with virtualenv and 
MySQL database server


## Build / Run 
-> create and activate a python virtualenv

-> `$ pip install -r requirements.txt`

-> `$ nano .env`

-> enter values for env variables in .env file (replaced with your db credentials) :
```
MYSQL_DB_NAME = DATABASE_NAME
MYSQL_DB_HOST = DATABASE_HOST
MYSQL_DB_USERNAME = DATABASE_USER
MYSQL_DB_USERNAME = DATABASE_PASSWORD
DOMAIN_NAME = your own domain name
```
-> Note that you need to create an empty database (for DATABASE_NAME ) on your DB server.

-> `$ export FLASK_APP=url_shortener_app.py

->  $ flask db upgrade

->  $ gunicorn --bind 127.0.0.1:5000 wsgi:app_instance

-> app will be live on `127.0.0.1:5000`


#### Developer contact
 - [ github ](https://github.com/sanskarsharma)
 - [ linkedin ](https://linkedin.com/in/sanskarssh)
 - [angel](https://angel.co/sanskarsharma)

     
