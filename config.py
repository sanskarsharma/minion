import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-easily-guess'

    SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        os.environ.get('DB_VENDOR'),
        os.environ.get('DB_USERNAME'),
        os.environ.get('DB_PASSWORD'),
        os.environ.get('DB_HOST'),
        os.environ.get('DB_PORT'),
        os.environ.get('DB_NAME')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DOMAIN_NAME= os.environ.get('DOMAIN_NAME', 'minion')
