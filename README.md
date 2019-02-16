
# minion - url shortener webapp

This is a utility app for minifying long urls. 
Demo is live on http://m96.pythonanywhere.com

## About project
- made using python Flask framework.
- Database used is MySQL, managed by SQLAlchemy
- docker used for simplified deployment

## Prerequisites for setup
docker


## Build / Run 
-> cd /minion 

-> `$ nano mysql.env`

-> enter below values for env variables in mysql.env file (replaced with db credentials that you want to give for your mysql server) :
```
MYSQL_RANDOM_ROOT_PASSWORD=yes
MYSQL_USER=<blah>
MYSQL_PASSWORD=<meh>
MYSQL_DATABASE=<duh>
```

-> `$ nano .env`


-> enter below values for env variables in .env file (replaced with db credentials that you want to give for your mysql server) :
```
DB_VENDOR=mysql+pymysql
DB_HOST=dbserverboi
DB_PORT=3306
DB_USERNAME=<blah>
DB_PASSWORD=<meh>
DB_NAME=<duh>

SECRET_KEY=<blet>
```

`$ docker run --name mysqlboi -d --env-file mysql.env mysql/mysql-server:5.7`

`$ docker run --name minionboi -d -p 8000:5665 --rm  --env-file=.env --link mysqlboi:dbserverboi sanskarsharma/minion:latest`





-> app will be live on `0.0.0.0:8000`


#### Developer contact
 - [ github ](https://github.com/sanskarsharma)
 - [ linkedin ](https://linkedin.com/in/sanskarssh)
 - [angel](https://angel.co/sanskarsharma)

