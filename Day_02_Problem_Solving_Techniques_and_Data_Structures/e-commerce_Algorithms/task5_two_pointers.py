# ==========================================
# TASK 5: TWO POINTERS
# E-Commerce Gift Card Pair Finder
# ==========================================

# Sorted order values
order_values = [
    100, 150, 200, 250, 300,
    350, 400, 450, 500, 550
]

# Gift card target value
target = 700


# ==========================================
# TWO POINTERS ALGORITHM
# ==========================================

left = 0
right = len(order_values) - 1

pairs = []

while left < right:

    current_sum = order_values[left] + order_values[right]

    if current_sum == target:

        pairs.append((order_values[left], order_values[right]))

        left += 1
        right -= 1

    elif current_sum < target:

        left += 1

    else:

        right -= 1


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("=" * 50)
print("GIFT CARD PAIR FINDER")
print("=" * 50)

print("\nOrder Values:")
print(order_values)

print(f"\nGift Card Value: ₹{target}")

print("\nMatching Pairs:")

if pairs:

    for pair in pairs:
        print(f"₹{pair[0]} + ₹{pair[1]} = ₹{target}")

else:

    print("No matching pairs found.")

print(f"\nTotal Matching Pairs: {len(pairs)}")