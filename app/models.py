from datetime import datetime
from app import db_instance


class Links(db_instance.Model):
    id = db_instance.Column(db_instance.Integer, primary_key=True)
    long_url = db_instance.Column(db_instance.String(1000))
    short_url = db_instance.Column(db_instance.String(64), unique=True)
    count = db_instance.Column(db_instance.Integer)

