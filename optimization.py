from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpInteger
from models import Patient, Resource, db

def optimize_allocations():
    # Fetch data
    patients = Patient.query.all()
    resources = Resource.query.all()

    # Create problem
    prob = LpProblem("Hospital_Resource_Allocation", LpMinimize)

    # Decision variables: allocation of resource to patient
    allocations = {}
    for patient in patients:
        for resource in resources:
            allocations[(patient.id, resource.id)] = LpVariable(f"alloc_{patient.id}_{resource.id}", 0, 1, LpInteger)

    # Objective: Minimize total wait time
    prob += lpSum([patient.priority * patient.wait_time for patient in patients])

    # Constraints
    # Resource availability
    for resource in resources:
        prob += lpSum([allocations[(p.id, resource.id)] for p in patients]) <= resource.available

    # Patient needs
    for patient in patients:
        if patient.bed_needed:
            bed_resource = next((r for r in resources if r.type == 'bed'), None)
            if bed_resource:
                prob += allocations[(patient.id, bed_resource.id)] == 1
        if patient.doctor_needed:
            doctor_resource = next((r for r in resources if r.type == 'doctor'), None)
            if doctor_resource:
                prob += allocations[(patient.id, doctor_resource.id)] == 1
        if patient.equipment_needed:
            equip_resource = next((r for r in resources if r.type == 'equipment'), None)
            if equip_resource:
                prob += allocations[(patient.id, equip_resource.id)] == 1

    # Solve
    prob.solve()

    # Update allocations
    for patient in patients:
        for resource in resources:
            if allocations[(patient.id, resource.id)].value() == 1:
                resource.allocated += 1
                patient.wait_time = 0  # Assume allocated immediately for simplicity

    db.session.commit()

    return {p.id: [r.type for r in resources if allocations[(p.id, r.id)].value() == 1] for p in patients}
