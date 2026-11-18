# ==========================================
# TASK 4: SLIDING WINDOW
# E-Commerce Peak Traffic Analysis
# ==========================================

# Requests received per hour for 24 hours
requests = [
    120, 150, 180, 200, 220, 250,
    300, 450, 600, 750, 900, 850,
    700, 650, 500, 400, 350, 300,
    250, 200, 180, 160, 140, 130
]

window_size = 3

# ==========================================
# INITIAL WINDOW
# ==========================================

current_sum = sum(requests[:window_size])

max_sum = current_sum

max_start = 0

# ==========================================
# SLIDING WINDOW
# ==========================================

for i in range(window_size, len(requests)):

    # Remove the outgoing element
    current_sum -= requests[i - window_size]

    # Add the incoming element
    current_sum += requests[i]

    # Update maximum
    if current_sum > max_sum:
        max_sum = current_sum
        max_start = i - window_size + 1


# ==========================================
# DISPLAY RESULTS
# ==========================================

start_hour = max_start
end_hour = max_start + window_size - 1

print("=" * 50)
print("E-COMMERCE PEAK TRAFFIC ANALYSIS")
print("=" * 50)

print("\nHourly Requests:")
for hour, count in enumerate(requests):
    print(f"Hour {hour:02d}:00 - {count} requests")

print("\nBusiest 3-Hour Window:")
print(f"Start Hour: {start_hour:02d}:00")
print(f"End Hour: {end_hour + 1:02d}:00")

print("\nRequests During Busiest Window:")
print(requests[max_start:max_start + window_size])

print(f"\nTotal Requests: {max_sum}")

print("\nInfrastructure Recommendation:")
print("Increase server capacity during this peak period.")