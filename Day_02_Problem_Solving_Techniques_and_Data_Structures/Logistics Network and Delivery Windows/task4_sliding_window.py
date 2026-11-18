# Logistics Network and Delivery Windows
# Task 4: Sliding Window
# Find the 4-hour window with the highest average parcel count

def highest_average_window(parcels, window_size):

    # Handle invalid input
    if not parcels or window_size > len(parcels) or window_size <= 0:
        return None

    # Calculate the sum of the first window
    current_sum = sum(parcels[:window_size])

    max_sum = current_sum
    best_start = 0

    # Slide the window
    for i in range(window_size, len(parcels)):

        # Remove the outgoing hour
        current_sum -= parcels[i - window_size]

        # Add the incoming hour
        current_sum += parcels[i]

        # Update maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i - window_size + 1

    best_window = parcels[best_start:best_start + window_size]
    average = max_sum / window_size

    return best_window, best_start, max_sum, average


# -----------------------------------
# Main Program
# -----------------------------------

print("=" * 55)
print("LOGISTICS NETWORK MANAGEMENT")
print("TASK 4: SLIDING WINDOW")
print("=" * 55)

# Hourly parcel counts
hourly_parcels = [
    120, 150, 180, 200,
    250, 300, 350, 400,
    280, 220, 190, 170
]

window_size = 4

print("\nHourly Parcel Counts:")
print(hourly_parcels)

print(f"\nWindow Size: {window_size} hours")

# Find highest average window
result = highest_average_window(hourly_parcels, window_size)

if result:

    best_window, start_index, max_sum, average = result

    print("\n" + "-" * 55)
    print("HIGHEST AVERAGE 4-HOUR WINDOW")
    print("-" * 55)

    print("Parcel Counts:", best_window)

    print(f"Starting Hour: {start_index + 1}")
    print(f"Ending Hour: {start_index + window_size}")

    print("Total Parcels:", max_sum)
    print(f"Average Parcels per Hour: {average:.2f}")

else:
    print("Invalid input or insufficient hourly data.")


# -----------------------------------
# Test Cases
# -----------------------------------

print("\n" + "-" * 55)
print("TEST CASES")
print("-" * 55)

# Test Case 1: Normal input
print("\nTest Case 1:")
print(highest_average_window([10, 20, 30, 40, 50], 4))

# Test Case 2: Empty input
print("\nTest Case 2 - Empty List:")
print(highest_average_window([], 4))

# Test Case 3: Window larger than list
print("\nTest Case 3 - Invalid Window:")
print(highest_average_window([10, 20], 4))

# Test Case 4: All values equal
print("\nTest Case 4 - Equal Values:")
print(highest_average_window([10, 10, 10, 10, 10], 4))

# Test Case 5: Window size 1
print("\nTest Case 5 - Window Size 1:")
print(highest_average_window([10, 50, 20, 40], 1))

print("\n" + "=" * 55)
print("PROGRAM COMPLETED")
print("=" * 55)