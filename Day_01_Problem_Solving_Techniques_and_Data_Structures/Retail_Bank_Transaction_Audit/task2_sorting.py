import csv
import time

# Read transactions from CSV
transactions = []

with open("transactions.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        transactions.append(row)


# Use only 1000 records for Insertion Sort
insertion_data = transactions[:1000]

# Use all 100000 records for Merge Sort
merge_data = transactions.copy()


# ---------------- INSERTION SORT ----------------

def insertion_sort(data):
    arr = data.copy()

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j]["posting_date"] > key["posting_date"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# ---------------- MERGE SORT ----------------

def merge_sort(data):

    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i]["posting_date"] <= right[j]["posting_date"]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---------------- PERFORMANCE COMPARISON ----------------

start = time.time()

sorted_insertion = insertion_sort(insertion_data)

insertion_time = time.time() - start


start = time.time()

sorted_merge = merge_sort(merge_data)

merge_time = time.time() - start


# ---------------- OUTPUT ----------------

print("=" * 60)
print("BANK TRANSACTION STATEMENT SORTING")
print("=" * 60)

print("\nInsertion Sort")
print("Records sorted:", len(sorted_insertion))
print(f"Execution time: {insertion_time:.6f} seconds")

print("\nMerge Sort")
print("Records sorted:", len(sorted_merge))
print(f"Execution time: {merge_time:.6f} seconds")


print("\nFirst 10 Transactions Sorted by Posting Date:")

for transaction in sorted_merge[:10]:

    print(
        transaction["transaction_id"],
        transaction["account_id"],
        transaction["amount"],
        transaction["merchant"],
        transaction["posting_date"]
    )


# ---------------- STABILITY DEMONSTRATION ----------------

print("\nSTABILITY CHECK")

same_date_transactions = [
    transaction
    for transaction in sorted_merge
    if transaction["posting_date"] == sorted_merge[0]["posting_date"]
]

for transaction in same_date_transactions[:5]:
    print(
        transaction["transaction_id"],
        transaction["posting_date"]
    )