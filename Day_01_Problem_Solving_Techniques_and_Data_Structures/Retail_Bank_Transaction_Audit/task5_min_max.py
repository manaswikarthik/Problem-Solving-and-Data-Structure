import csv
import time

# Read transaction amounts from CSV
amounts = []

with open("transactions.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        amounts.append(float(row["amount"]))


# ==========================================
# BRUTE FORCE APPROACH
# ==========================================

def brute_force_min_max(arr):

    minimum = arr[0]
    maximum = arr[0]

    for num in arr:

        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return minimum, maximum


# ==========================================
# DIVIDE AND CONQUER APPROACH
# ==========================================

def divide_conquer_min_max(arr, low, high):

    # Base case: only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        else:
            return arr[high], arr[low]

    # Divide the array
    mid = (low + high) // 2

    left_min, left_max = divide_conquer_min_max(
        arr, low, mid
    )

    right_min, right_max = divide_conquer_min_max(
        arr, mid + 1, high
    )

    # Combine results
    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)

    return minimum, maximum


# ==========================================
# PERFORMANCE COMPARISON
# ==========================================

# Brute Force
start = time.time()

brute_min, brute_max = brute_force_min_max(amounts)

brute_time = time.time() - start


# Divide and Conquer
start = time.time()

dc_min, dc_max = divide_conquer_min_max(
    amounts, 0, len(amounts) - 1
)

dc_time = time.time() - start


# ==========================================
# OUTPUT
# ==========================================

print("=" * 60)
print("BANK TRANSACTION MINIMUM AND MAXIMUM ANALYSIS")
print("=" * 60)

print("Total Transactions:", len(amounts))

print("\nBRUTE FORCE")
print("Minimum Amount:", brute_min)
print("Maximum Amount:", brute_max)
print(f"Execution Time: {brute_time:.6f} seconds")

print("\nDIVIDE AND CONQUER")
print("Minimum Amount:", dc_min)
print("Maximum Amount:", dc_max)
print(f"Execution Time: {dc_time:.6f} seconds")

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

if brute_min == dc_min and brute_max == dc_max:
    print("Both approaches produced the same result.")

print("Brute Force Time:", brute_time)
print("Divide and Conquer Time:", dc_time)