import csv
import time

# Load appointments from CSV
with open("appointments.csv", "r") as file:
    reader = csv.DictReader(file)
    appointments = list(reader)

# Urgency ranking
urgency_rank = {
    "Critical": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4
}

# Sorting key: urgency first, arrival time second
def sort_key(appointment):
    return (
        urgency_rank[appointment["urgency"]],
        appointment["arrival_time"]
    )


# ---------------- SELECTION SORT ----------------

def selection_sort(data):
    arr = data.copy()
    swaps = 0

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if sort_key(arr[j]) < sort_key(arr[min_index]):
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, swaps


# ---------------- QUICK SORT ----------------

def quick_sort(data):
    arr = data.copy()
    swaps = 0

    def partition(low, high):
        nonlocal swaps

        pivot = sort_key(arr[high])
        i = low - 1

        for j in range(low, high):
            if sort_key(arr[j]) <= pivot:
                i += 1

                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1

        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps += 1

        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)

            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    quick_sort_recursive(0, len(arr) - 1)

    return arr, swaps


# ---------------- EXECUTION ----------------

# Selection Sort
start = time.time()
selection_result, selection_swaps = selection_sort(appointments)
selection_time = time.time() - start

# Quick Sort
start = time.time()
quick_result, quick_swaps = quick_sort(appointments)
quick_time = time.time() - start


# ---------------- RESULTS ----------------

print("=" * 60)
print("HOSPITAL APPOINTMENT SORTING")
print("=" * 60)

print(f"Total appointments: {len(appointments)}")

print("\nSELECTION SORT")
print(f"Execution time: {selection_time:.6f} seconds")
print(f"Number of swaps: {selection_swaps}")

print("\nQUICK SORT")
print(f"Execution time: {quick_time:.6f} seconds")
print(f"Number of swaps: {quick_swaps}")

print("\nFIRST 10 SORTED APPOINTMENTS")
print("-" * 60)

for appointment in quick_result[:10]:
    print(
        appointment["patient_id"],
        appointment["doctor"],
        appointment["urgency"],
        appointment["arrival_time"],
        appointment["duration"]
    )

print("\n" + "=" * 60)