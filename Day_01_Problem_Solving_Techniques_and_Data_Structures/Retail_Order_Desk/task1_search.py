import csv
import time

# -------------------------------
# 1. Load orders from CSV
# -------------------------------
def load_orders(filename):
    orders = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["orderId"] = int(row["orderId"])
            row["customerId"] = int(row["customerId"])
            row["amount"] = float(row["amount"])

            orders.append(row)

    return orders


# -------------------------------
# 2. Linear Search
# -------------------------------
def linear_search(orders, target_id):
    for order in orders:
        if order["orderId"] == target_id:
            return order

    return None


# -------------------------------
# 3. Binary Search
# -------------------------------
def binary_search(orders, target_id):
    low = 0
    high = len(orders) - 1

    while low <= high:
        mid = (low + high) // 2

        if orders[mid]["orderId"] == target_id:
            return orders[mid]

        elif orders[mid]["orderId"] < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# -------------------------------
# 4. Main Program
# -------------------------------
orders = load_orders("orders.csv")

target_id = 45000

print("=" * 60)
print("             RETAIL ORDER SEARCH SYSTEM")
print("=" * 60)

print(f"\nTotal orders loaded: {len(orders)}")
print(f"Searching for Order ID: {target_id}")


# Linear Search Benchmark
start_time = time.perf_counter()

linear_result = linear_search(orders, target_id)

linear_time = time.perf_counter() - start_time


# Sort orders before Binary Search
sorted_orders = sorted(orders, key=lambda order: order["orderId"])


# Binary Search Benchmark
start_time = time.perf_counter()

binary_result = binary_search(sorted_orders, target_id)

binary_time = time.perf_counter() - start_time


# -------------------------------
# 5. Display Results
# -------------------------------
print("\n--- Linear Search ---")

if linear_result:
    print("Order Found:", linear_result)
else:
    print("Order not found.")

print(f"Execution Time: {linear_time:.8f} seconds")


print("\n--- Binary Search ---")

if binary_result:
    print("Order Found:", binary_result)
else:
    print("Order not found.")

print(f"Execution Time: {binary_time:.8f} seconds")


# -------------------------------
# 6. Performance Comparison
# -------------------------------
print("\n--- Performance Comparison ---")

print(f"Linear Search : {linear_time:.8f} seconds")
print(f"Binary Search : {binary_time:.8f} seconds")

if linear_time > binary_time:
    difference = linear_time / binary_time

    print(f"\nBinary Search was approximately {difference:.2f} times faster.")

else:
    print("\nLinear Search was faster in this particular execution.")

print("=" * 60)