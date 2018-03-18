from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app_instance = Flask(__name__)

app_instance.config.from_object(Config)


db_instance = SQLAlchemy(app_instance)
migrate = Migrate(app_instance,db_instance)


from app import routes, models
