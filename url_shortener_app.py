from app import app_instance, db_instance
from app.models import Links

@app_instance.shell_context_processor
def make_shell_context():
    return {'db': db_instance, 'Links': Links}
