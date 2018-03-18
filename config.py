import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-easily-guess'

    MYSQL_DB_USERNAME = os.environ.get("MYSQL_DB_USERNAME")
    MYSQL_DB_PASSWORD = os.environ.get("MYSQL_DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + MYSQL_DB_USERNAME + ":" + MYSQL_DB_PASSWORD + "@localhost/urlshortener"
    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql.2996@localhost/urlshortener"
    

    #  os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DOMAIN_NAME= "sanskarsharma.tech"