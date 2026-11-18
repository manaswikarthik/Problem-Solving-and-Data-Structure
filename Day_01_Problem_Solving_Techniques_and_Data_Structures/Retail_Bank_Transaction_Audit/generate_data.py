import csv
import random
from datetime import datetime, timedelta

NUM_TRANSACTIONS = 100000

merchants = ["Amazon", "Flipkart", "Swiggy", "Zomato", "Reliance", "DMart", "Uber", "IRCTC"]

start_date = datetime(2026, 1, 1)

rows = []

for i in range(1, NUM_TRANSACTIONS + 1):

    account_id = random.randint(1000, 9999)
    amount = round(random.uniform(100, 50000), 2)
    merchant = random.choice(merchants)

    posting_date = start_date + timedelta(
        seconds=random.randint(0, 86400 * 30)
    )

    rows.append([
        i,
        account_id,
        amount,
        merchant,
        posting_date.strftime("%Y-%m-%d %H:%M:%S")
    ])

with open("transactions.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "transaction_id",
        "account_id",
        "amount",
        "merchant",
        "posting_date"
    ])

    writer.writerows(rows)

print("Dataset generated successfully!")
print(f"Total transactions: {NUM_TRANSACTIONS}")