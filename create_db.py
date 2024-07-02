from app import app, db

# Ensure you import your models here
from app.models import User

with app.app_context():
    db.create_all()
    print("Database initialized and tables created.")
