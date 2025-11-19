import requests

# Test adding a patient
data = {'name': 'John Doe', 'priority': '8', 'bed': 'bed', 'doctor': 'doctor'}
response = requests.post('http://127.0.0.1:5000/add_patient', data=data)
print('Add patient status:', response.status_code)

# Test getting allocations
response = requests.get('http://127.0.0.1:5000/allocations')
print('Allocations page status:', response.status_code)
print('Content length:', len(response.text))

# Add another patient
data2 = {'name': 'Jane Smith', 'priority': '5', 'equipment': 'equipment'}
response2 = requests.post('http://127.0.0.1:5000/add_patient', data=data2)
print('Add second patient status:', response2.status_code)

# Check allocations again
response3 = requests.get('http://127.0.0.1:5000/allocations')
print('Allocations page status after second patient:', response3.status_code)
print('Content length:', len(response3.text))
