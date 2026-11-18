import csv
import random
from datetime import datetime, timedelta

# Number of orders
NUM_ORDERS = 50000

# Output file
filename = "orders.csv"

# Generate sample orders
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    # CSV header
    writer.writerow(["orderId", "customerId", "amount", "createdAt"])

    start_date = datetime(2026, 1, 1)

    for i in range(1, NUM_ORDERS + 1):

        order_id = i
        customer_id = random.randint(1000, 10000)
        amount = round(random.uniform(100, 10000), 2)

        created_at = start_date + timedelta(
            minutes=random.randint(0, 525600)
        )

        writer.writerow([
            order_id,
            customer_id,
            amount,
            created_at.strftime("%Y-%m-%d %H:%M:%S")
        ])

print(f"{NUM_ORDERS} orders generated successfully!")
print(f"File created: {filename}")