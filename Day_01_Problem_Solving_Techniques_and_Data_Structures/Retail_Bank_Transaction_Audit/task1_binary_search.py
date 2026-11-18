import time

# Generate sorted transaction IDs
transaction_ids = list(range(1, 100001))


# Linear Search
def linear_search(data, target):
    comparisons = 0

    for transaction_id in data:
        comparisons += 1

        if transaction_id == target:
            return True, comparisons

    return False, comparisons


# Binary Search
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if data[mid] == target:
            return True, comparisons

        elif data[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return False, comparisons


# Test cases
targets = {
    "Best Case": 50000,
    "Average Case": 75000,
    "Worst Case": 100000
}

print("TRANSACTION ID SEARCH COMPARISON")
print("-" * 50)

for case, target in targets.items():

    found_linear, linear_comparisons = linear_search(
        transaction_ids, target
    )

    found_binary, binary_comparisons = binary_search(
        transaction_ids, target
    )

    print(f"\n{case}")
    print(f"Target ID: {target}")
    print(f"Linear Search Comparisons: {linear_comparisons}")
    print(f"Binary Search Comparisons: {binary_comparisons}")


# Time comparison
target = 100000

start = time.time()
linear_search(transaction_ids, target)
linear_time = time.time() - start

start = time.time()
binary_search(transaction_ids, target)
binary_time = time.time() - start

print("\n" + "-" * 50)
print("TIME COMPARISON")
print(f"Linear Search Time: {linear_time:.6f} seconds")
print(f"Binary Search Time: {binary_time:.6f} seconds")