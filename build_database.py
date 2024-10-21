# build_database.py

import os
from config import app, db
from models import Person

PEOPLE = [
    {"fname": "Doug", "lname": "Farrell"},
    {"fname": "Kent", "lname": "Brockman"},
    {"fname": "Bunny", "lname": "Easter"},
]

# Optional: Remove existing database file to start fresh
# Uncomment the following lines if you want to delete the existing database
# db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'people.db')
# if os.path.exists(db_path):
#     os.remove(db_path)

# Create the database tables and add sample data within the application context
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")

    # Add sample data
    for person in PEOPLE:
        p = Person(lname=person['lname'], fname=person['fname'])
        db.session.add(p)
    db.session.commit()
    print("Sample data added to the database.")
