import csv
from collections import defaultdict

# Load appointments
with open("appointments.csv", "r") as file:
    reader = csv.DictReader(file)
    appointments = list(reader)

# Hash set to track booked slots
booked_slots = set()

# Store duplicate appointments
duplicates = []

for appointment in appointments:

    # Unique key using patient ID and appointment time
    key = (
        appointment["patient_id"],
        appointment["arrival_time"]
    )

    if key in booked_slots:
        duplicates.append(appointment)
    else:
        booked_slots.add(key)


# Display results
print("=" * 50)
print("DOUBLE-BOOKED APPOINTMENT DETECTION")
print("=" * 50)

print(f"Total appointments checked: {len(appointments)}")
print(f"Duplicate appointments found: {len(duplicates)}")

if duplicates:
    print("\nDuplicate Appointments:")
    print("-" * 50)

    for appointment in duplicates:
        print(
            f"Patient ID: {appointment['patient_id']} | "
            f"Doctor: {appointment['doctor']} | "
            f"Arrival: {appointment['arrival_time']} | "
            f"Urgency: {appointment['urgency']}"
        )
else:
    print("\nNo double-booked appointments found.")

print("=" * 50)