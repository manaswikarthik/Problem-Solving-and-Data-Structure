import csv
import random
from datetime import datetime, timedelta

NUM_PATIENTS = 20000
NUM_APPOINTMENTS = 10000

doctors = [
    "Dr. Arun",
    "Dr. Priya",
    "Dr. Kumar",
    "Dr. Meera",
    "Dr. Sanjay"
]

urgency_levels = ["Low", "Medium", "High", "Critical"]

start_date = datetime(2026, 11, 18, 8, 0, 0)

# ==========================================
# GENERATE PATIENT DATA
# ==========================================

patients = []

for i in range(1, NUM_PATIENTS + 1):

    patients.append([
        i,
        f"Patient_{i}",
        random.randint(18, 85),
        random.choice(["Male", "Female"]),
        f"90000{random.randint(10000, 99999)}"
    ])


with open("patients.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "patient_id",
        "patient_name",
        "age",
        "gender",
        "phone"
    ])

    writer.writerows(patients)


# ==========================================
# GENERATE APPOINTMENT DATA
# ==========================================

appointments = []

for i in range(1, NUM_APPOINTMENTS + 1):

    patient_id = random.randint(1, NUM_PATIENTS)

    doctor = random.choice(doctors)

    urgency = random.choice(urgency_levels)

    arrival_time = start_date + timedelta(
        minutes=random.randint(0, 600)
    )

    duration = random.choice([15, 30, 45, 60])

    appointment_slot = arrival_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    appointments.append([
        i,
        patient_id,
        doctor,
        urgency,
        appointment_slot,
        duration
    ])


with open("appointments.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "appointment_id",
        "patient_id",
        "doctor",
        "urgency",
        "arrival_time",
        "duration"
    ])

    writer.writerows(appointments)


print("Hospital dataset generated successfully!")
print("Total patients:", NUM_PATIENTS)
print("Total appointments:", NUM_APPOINTMENTS)