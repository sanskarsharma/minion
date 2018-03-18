from url_shortener_app import app_instance

if __name__ == "__main__":
    app_instance.run()


# command for running gunicorn
# gunicorn --bind 0.0.0.0:8080 wsgi:app_instance



# sudo ln -s /etc/nginx/sites-available/flask_microblog /etc/nginx/sites-enabled