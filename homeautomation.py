from app import app,db
from app.models import Device

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Device': Device }
