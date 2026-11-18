import csv
from datetime import datetime

# Read transactions
transactions = []

with open("transactions.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        transactions.append(row)


# Duplicate detection
def detect_duplicates(transactions):

    seen = {}
    duplicates = []

    for transaction in transactions:

        account_id = transaction["account_id"]
        amount = transaction["amount"]
        merchant = transaction["merchant"]

        timestamp = datetime.strptime(
            transaction["posting_date"],
            "%Y-%m-%d %H:%M:%S"
        )

        # Create a key using account, amount and merchant
        key = (account_id, amount, merchant)

        if key in seen:

            previous_timestamp = seen[key]

            time_difference = abs(
                (timestamp - previous_timestamp).total_seconds()
            )

            if time_difference <= 60:
                duplicates.append(transaction)

        # Store latest timestamp
        seen[key] = timestamp

    return duplicates


# Execute
duplicates = detect_duplicates(transactions)


# Display results
print("=" * 50)
print("DUPLICATE TRANSACTION DETECTION")
print("=" * 50)

print("Total transactions:", len(transactions))
print("Duplicate transactions detected:", len(duplicates))

print("\nDuplicate Records:\n")

for transaction in duplicates[:10]:

    print(
        "Transaction ID:", transaction["transaction_id"],
        "| Account:", transaction["account_id"],
        "| Amount:", transaction["amount"],
        "| Merchant:", transaction["merchant"],
        "| Date:", transaction["posting_date"]
    )