import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-easily-guess'

    MYSQL_DB_HOST = os.environ.get("MYSQL_DB_HOST")
    MYSQL_DB_NAME = os.environ.get("MYSQL_DB_NAME")

    MYSQL_DB_USERNAME = os.environ.get("MYSQL_DB_USERNAME")
    MYSQL_DB_PASSWORD = os.environ.get("MYSQL_DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + MYSQL_DB_USERNAME + ":" + MYSQL_DB_PASSWORD + "@"+ MYSQL_DB_HOST +"/" + MYSQL_DB_NAME

#    MYSQL_DB_USERNAME = os.environ.get("MYSQL_DB_USERNAME")
#    MYSQL_DB_PASSWORD = os.environ.get("MYSQL_DB_PASSWORD")
#    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + MYSQL_DB_USERNAME + ":" + MYSQL_DB_PASSWORD + "@localhost/urlshortener"
    
    

    #  os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DOMAIN_NAME= os.environ.get("DOMAIN_NAME")
