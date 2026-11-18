import time
import random

# ==========================================
# CUSTOM HASH TABLE USING CHAINING
# ==========================================

class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)

        # Handle duplicate keys
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return

        self.table[index].append([key, value])

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None

    # Display hash table
    def display(self):
        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")


# ==========================================
# TASK 1: DEMONSTRATE HASHING AND COLLISION
# ==========================================

print("=" * 60)
print("CUSTOM HASH TABLE - SKU LOOKUP")
print("=" * 60)

ht = HashTable(size=10)

# Insert sample products
ht.insert("SKU101", "Laptop")
ht.insert("SKU102", "Mobile")
ht.insert("SKU103", "Headphones")
ht.insert("SKU104", "Keyboard")
ht.insert("SKU105", "Mouse")

print("\nHash Table:")
ht.display()

# Search
print("\nSearch Results:")
print("SKU101:", ht.search("SKU101"))
print("SKU103:", ht.search("SKU103"))
print("SKU999:", ht.search("SKU999"))


# ==========================================
# TASK 2: DEMONSTRATE COLLISION
# ==========================================

print("\n" + "=" * 60)
print("COLLISION DEMONSTRATION")
print("=" * 60)

collision_ht = HashTable(size=10)

collision_ht.insert("AB", "Product A")
collision_ht.insert("BA", "Product B")

print("\nHash Index of AB:", collision_ht.hash_function("AB"))
print("Hash Index of BA:", collision_ht.hash_function("BA"))

print("\nHash Table After Collision:")
collision_ht.display()


# ==========================================
# TASK 3: PERFORMANCE COMPARISON
# ==========================================

print("\n" + "=" * 60)
print("PERFORMANCE COMPARISON - 100,000 SKUs")
print("=" * 60)

number_of_skus = 100000

# Generate SKU data
products = {
    f"SKU{i}": f"Product{i}"
    for i in range(number_of_skus)
}

# Custom hash table
custom_ht = HashTable(size=200003)

print("\nBuilding Custom Hash Table...")

for key, value in products.items():
    custom_ht.insert(key, value)

print("Custom Hash Table Created Successfully!")

# Prepare random lookup keys
search_keys = random.sample(list(products.keys()), 10000)

# ------------------------------------------
# Custom Hash Table Lookup Time
# ------------------------------------------

start_time = time.perf_counter()

for key in search_keys:
    custom_ht.search(key)

custom_time = time.perf_counter() - start_time


# ------------------------------------------
# Python Dictionary Lookup Time
# ------------------------------------------

start_time = time.perf_counter()

for key in search_keys:
    products.get(key)

dictionary_time = time.perf_counter() - start_time


# ------------------------------------------
# Display Results
# ------------------------------------------

print("\nLookup Results for 10,000 Searches")

print(f"Custom Hash Table: {custom_time:.6f} seconds")

print(f"Python Dictionary: {dictionary_time:.6f} seconds")

if custom_time > dictionary_time:
    print("\nPython Dictionary is faster.")
else:
    print("\nCustom Hash Table is faster.")