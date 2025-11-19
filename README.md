# Apollo Hospitals - AI-Based Resource Allocation System

This is a minor project demonstrating an AI-based system for allocating hospital resources (beds, doctors, equipment) to patients, optimizing to minimize wait times.

## Features
- Add patients with priority and resource needs.
- AI optimization using linear programming to allocate resources.
- View current allocations and resource status.

## Tech Stack
- Flask (web framework)
- SQLite (database)
- PuLP (optimization library)

## Setup
1. Create virtual environment: `python -m venv venv`
2. Activate: `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open http://127.0.0.1:5000/

## Usage
- Go to home page to add a patient.
- Select needed resources and priority.
- Submit to allocate and view results.
