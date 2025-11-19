from app import app, db, Patient, Resource

with app.app_context():
    patients = Patient.query.all()
    resources = Resource.query.all()
    print('Patients:')
    for p in patients:
        print(f'  {p.name} (Priority: {p.priority}) - Needs: Bed:{p.bed_needed}, Doctor:{p.doctor_needed}, Equip:{p.equipment_needed}')
    print('Resources:')
    for r in resources:
        print(f'  {r.type}: Available {r.available}, Allocated {r.allocated}')
