from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.Integer, nullable=False)  # 1-10, higher is more urgent
    bed_needed = db.Column(db.Boolean, default=False)
    doctor_needed = db.Column(db.Boolean, default=False)
    equipment_needed = db.Column(db.Boolean, default=False)
    wait_time = db.Column(db.Integer, default=0)  # in hours

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # 'bed', 'doctor', 'equipment'
    available = db.Column(db.Integer, nullable=False)
    allocated = db.Column(db.Integer, default=0)
