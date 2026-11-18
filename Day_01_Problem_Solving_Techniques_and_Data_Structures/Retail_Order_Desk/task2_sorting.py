import csv
import time


# --------------------------------
# 1. Load orders from CSV
# --------------------------------
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


# --------------------------------
# 2. Bubble Sort
# Sort by amount in descending order
# --------------------------------
def bubble_sort(orders):
    arr = orders.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j]["amount"] < arr[j + 1]["amount"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# --------------------------------
# 3. Merge Sort
# --------------------------------
def merge_sort(orders):

    if len(orders) <= 1:
        return orders

    mid = len(orders) // 2

    left = merge_sort(orders[:mid])
    right = merge_sort(orders[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i]["amount"] >= right[j]["amount"]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# --------------------------------
# 4. Main Program
# --------------------------------
orders = load_orders("orders.csv")

# Use 10,000 records for benchmarking
test_orders = orders[:10000]

print("=" * 60)
print("              ORDER SORTING PERFORMANCE")
print("=" * 60)

print(f"\nNumber of records: {len(test_orders)}")


# --------------------------------
# Bubble Sort Benchmark
# --------------------------------
start = time.perf_counter()

bubble_result = bubble_sort(test_orders)

bubble_time = time.perf_counter() - start

print("\nBubble Sort:")
print(f"Execution Time: {bubble_time:.6f} seconds")


# --------------------------------
# Merge Sort Benchmark
# --------------------------------
start = time.perf_counter()

merge_result = merge_sort(test_orders)

merge_time = time.perf_counter() - start

print("\nMerge Sort:")
print(f"Execution Time: {merge_time:.6f} seconds")


# --------------------------------
# Built-in Sort Benchmark
# --------------------------------
start = time.perf_counter()

builtin_result = sorted(
    test_orders,
    key=lambda order: order["amount"],
    reverse=True
)

builtin_time = time.perf_counter() - start

print("\nPython Built-in Sort:")
print(f"Execution Time: {builtin_time:.6f} seconds")


# --------------------------------
# 5. Compare Results
# --------------------------------
print("\n--- Performance Comparison ---")

print(f"Bubble Sort : {bubble_time:.6f} seconds")
print(f"Merge Sort  : {merge_time:.6f} seconds")
print(f"Built-in Sort: {builtin_time:.6f} seconds")


# --------------------------------
# 6. Display Top 5 Orders
# --------------------------------
print("\n--- Top 5 Highest Amount Orders ---")

for order in builtin_result[:5]:
    print(
        f"Order ID: {order['orderId']} | "
        f"Amount: ₹{order['amount']}"
    )


print("=" * 60)