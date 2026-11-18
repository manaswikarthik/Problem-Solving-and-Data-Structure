import csv
from datetime import datetime, timedelta
import time

# Load appointments
with open("appointments.csv", "r") as file:
    reader = csv.DictReader(file)
    appointments = list(reader)

# Select one doctor
doctor_name = "Dr Arun"

doctor_appointments = []

for appointment in appointments:
    if appointment["doctor"] == doctor_name:
        doctor_appointments.append(appointment)


# Convert arrival time into datetime
def get_start(appointment):
    return datetime.strptime(
        appointment["arrival_time"],
        "%Y-%m-%d %H:%M:%S"
    )


def get_end(appointment):
    start = get_start(appointment)
    duration = int(appointment["duration"])

    return start + timedelta(minutes=duration)


# ==========================================
# DYNAMIC PROGRAMMING
# ==========================================

def dynamic_programming(appointments):

    # Sort by finishing time
    appointments = sorted(appointments, key=get_end)

    n = len(appointments)

    # Find previous compatible appointment
    previous = []

    for i in range(n):
        p = -1

        for j in range(i - 1, -1, -1):
            if get_end(appointments[j]) <= get_start(appointments[i]):
                p = j
                break

        previous.append(p)

    # DP table
    dp = [0] * n

    for i in range(n):
        include = 1

        if previous[i] != -1:
            include += dp[previous[i]]

        exclude = dp[i - 1] if i > 0 else 0

        dp[i] = max(include, exclude)

    return dp[-1] if n > 0 else 0


# ==========================================
# GREEDY ALGORITHM
# ==========================================

def greedy_algorithm(appointments):

    # Sort by finishing time
    appointments = sorted(appointments, key=get_end)

    selected = []
    last_end = None

    for appointment in appointments:

        start = get_start(appointment)
        end = get_end(appointment)

        if last_end is None or start >= last_end:
            selected.append(appointment)
            last_end = end

    return len(selected)


# ==========================================
# EXECUTION
# ==========================================

print("=" * 60)
print("HOSPITAL APPOINTMENT SCHEDULING")
print("=" * 60)

print(f"Doctor: {doctor_name}")
print(f"Total appointments: {len(doctor_appointments)}")


# Dynamic Programming
start_time = time.time()

dp_result = dynamic_programming(doctor_appointments)

dp_time = time.time() - start_time


# Greedy
start_time = time.time()

greedy_result = greedy_algorithm(doctor_appointments)

greedy_time = time.time() - start_time


# Results
print("\nDYNAMIC PROGRAMMING")
print(f"Maximum appointments: {dp_result}")
print(f"Execution time: {dp_time:.6f} seconds")


print("\nGREEDY ALGORITHM")
print(f"Maximum appointments: {greedy_result}")
print(f"Execution time: {greedy_time:.6f} seconds")


print("\nCOMPARISON")
print("-" * 60)

if dp_result == greedy_result:
    print("Both algorithms found the same maximum number of appointments.")
else:
    print("The algorithms produced different results.")

print("=" * 60)