from application import app
from application.models import db
with app.app_context():
    db.create_all()