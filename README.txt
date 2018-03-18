Install instructions :

This is a flask app which uses Gunicorn

1) make virtualenv using : python -m venv virtualenv
2) pip install -r requirements.txt
3) setup DB :
    -> make a database named urlshortener inside MySQL server on the same machine'
    -> enter values for env variables : MYSQL_DB_USERNAME and MYSQL_DB_PASSWORD from project directory    
    -> from project root directory run command : flask db upgrade
4) run project :
    -> gunicorn --bind 0.0.0.0:8080 wsgi:app_instance
