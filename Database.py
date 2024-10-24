import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('hospital_management.db')

# Create a cursor object
cursor = conn.cursor()

# Create tables for patients, staff, and appointments
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    patient_number INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    insurance TEXT,
    address TEXT,
    phone TEXT,
    registration_date TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS staff (
    staff_number INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    practicing_id TEXT,
    address TEXT,
    phone TEXT,
    registration_date TEXT,
    professional TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_number INTEGER,
    patient_first_name TEXT,
    staff_number INTEGER,
    staff_first_name TEXT,
    profession TEXT,
    appointment_date TEXT,
    FOREIGN KEY (patient_number) REFERENCES patients (patient_number),
    FOREIGN KEY (staff_number) REFERENCES staff (staff_number)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
