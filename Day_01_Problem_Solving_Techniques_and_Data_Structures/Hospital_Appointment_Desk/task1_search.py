import csv
import time
import random

# ==========================================
# LOAD PATIENT DATA
# ==========================================

patients = []

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        patients.append(row)

# Extract patient IDs
patient_ids = [int(patient["patient_id"]) for patient in patients]

# Binary search requires sorted data
patient_ids.sort()


# ==========================================
# LINEAR SEARCH
# ==========================================

def linear_search(data, target):

    for i in range(len(data)):

        if data[i] == target:
            return i

    return -1


# ==========================================
# BINARY SEARCH
# ==========================================

def binary_search(data, target):

    low = 0
    high = len(data) - 1

    while low <= high:

        mid = (low + high) // 2

        if data[mid] == target:
            return mid

        elif data[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# ==========================================
# GENERATE 1000 LOOKUPS
# ==========================================

search_targets = [
    random.randint(1, 20000)
    for _ in range(1000)
]


# ==========================================
# LINEAR SEARCH PERFORMANCE
# ==========================================

start = time.time()

for target in search_targets:
    linear_search(patient_ids, target)

linear_time = time.time() - start


# ==========================================
# BINARY SEARCH PERFORMANCE
# ==========================================

start = time.time()

for target in search_targets:
    binary_search(patient_ids, target)

binary_time = time.time() - start


# ==========================================
# TEST INDIVIDUAL SEARCH
# ==========================================

target = 15000

linear_result = linear_search(patient_ids, target)
binary_result = binary_search(patient_ids, target)


# ==========================================
# OUTPUT
# ==========================================

print("=" * 60)
print("HOSPITAL PATIENT SEARCH COMPARISON")
print("=" * 60)

print("Total Patient Records:", len(patient_ids))
print("Total Lookups:", len(search_targets))

print("\nIndividual Search Test")
print("Target Patient ID:", target)
print("Linear Search Result:", linear_result)
print("Binary Search Result:", binary_result)

print("\nPerformance for 1000 Lookups")

print(f"Linear Search Time: {linear_time:.6f} seconds")
print(f"Binary Search Time: {binary_time:.6f} seconds")

print("\nComparison")

if binary_time < linear_time:
    print("Binary Search is faster.")

else:
    print("Linear Search is faster.")

print("\nTime Complexity")
print("Linear Search: O(n)")
print("Binary Search: O(log n)")