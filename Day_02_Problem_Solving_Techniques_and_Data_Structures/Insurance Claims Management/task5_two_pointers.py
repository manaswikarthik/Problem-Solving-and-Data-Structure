# Insurance Claims Management
# Task 5: Merge Two Sorted Regional Claim Lists
# Algorithm: Two Pointers

def merge_claims(region_a, region_b):

    i = 0
    j = 0

    merged = []

    # Compare elements from both lists
    while i < len(region_a) and j < len(region_b):

        if region_a[i] < region_b[j]:
            merged.append(region_a[i])
            i += 1

        else:
            merged.append(region_b[j])
            j += 1

    # Add remaining elements from Region A
    while i < len(region_a):
        merged.append(region_a[i])
        i += 1

    # Add remaining elements from Region B
    while j < len(region_b):
        merged.append(region_b[j])
        j += 1

    return merged


# -------------------------------
# Main Program
# -------------------------------

print("=" * 50)
print("INSURANCE CLAIMS MANAGEMENT")
print("TASK 5: MERGE REGIONAL CLAIMS")
print("=" * 50)

# Regional claim lists
region_a = [101, 105, 110, 120, 135]
region_b = [102, 108, 115, 125, 140]

print("\nRegion A Claims:", region_a)
print("Region B Claims:", region_b)

# Merge the lists
result = merge_claims(region_a, region_b)

print("\nMerged Claims:")
print(result)

# -------------------------------
# Test Cases
# -------------------------------

print("\n" + "-" * 50)
print("TEST CASES")
print("-" * 50)

# Test Case 1: Normal input
print("\nTest Case 1 - Normal Input:")
print(merge_claims([10, 20, 30], [15, 25, 35]))

# Test Case 2: Empty first list
print("\nTest Case 2 - Empty Region A:")
print(merge_claims([], [10, 20, 30]))

# Test Case 3: Empty second list
print("\nTest Case 3 - Empty Region B:")
print(merge_claims([10, 20, 30], []))

# Test Case 4: Both lists empty
print("\nTest Case 4 - Both Lists Empty:")
print(merge_claims([], []))

# Test Case 5: Duplicate elements
print("\nTest Case 5 - Duplicate Claims:")
print(merge_claims([10, 20, 20, 40], [15, 20, 30]))

# Test Case 6: Unequal lengths
print("\nTest Case 6 - Unequal Lengths:")
print(merge_claims([5, 10], [1, 2, 3, 4, 6, 7, 8]))

print("\n" + "=" * 50)
print("PROGRAM COMPLETED")
print("=" * 50)