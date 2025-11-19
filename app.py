from flask import Flask, render_template, request, redirect, url_for
from models import db, Patient, Resource
from optimization import optimize_allocations

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
    # Initialize resources if not exist
    if not Resource.query.first():
        db.session.add(Resource(type='bed', available=10))
        db.session.add(Resource(type='doctor', available=5))
        db.session.add(Resource(type='equipment', available=20))
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@app.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)

@app.route('/add_resource', methods=['POST'])
def add_resource():
    type = request.form['type']
    available = int(request.form['available'])
    resource = Resource.query.filter_by(type=type).first()
    if resource:
        resource.available = available
    else:
        resource = Resource(type=type, available=available)
        db.session.add(resource)
    db.session.commit()
    return redirect(url_for('resources'))

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    priority = int(request.form['priority'])
    bed_needed = 'bed' in request.form
    doctor_needed = 'doctor' in request.form
    equipment_needed = 'equipment' in request.form
    patient = Patient(name=name, priority=priority, bed_needed=bed_needed, doctor_needed=doctor_needed, equipment_needed=equipment_needed)
    db.session.add(patient)
    db.session.commit()
    return redirect(url_for('allocations'))

@app.route('/allocations')
def allocations():
    allocations = optimize_allocations()
    patients = Patient.query.all()
    resources = Resource.query.all()
    return render_template('allocations.html', patients=patients, allocations=allocations, resources=resources)

if __name__ == '__main__':
    app.run(debug=True)
