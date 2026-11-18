# Insurance Claims Management
# Task 4: Claim Spike Analysis
# Algorithm: Sliding Window / Consecutive Run


# Daily claim counts
claims_per_day = [
    80, 120, 130, 150, 90,
    110, 115, 125, 140, 95,
    105, 108, 120, 80
]


# Threshold
threshold = 100


# Variables to track longest run
current_run = 0
longest_run = 0

start_day = 0
best_start_day = 0


# ------------------------------------------
# FIND LONGEST CONSECUTIVE RUN
# ------------------------------------------

for i in range(len(claims_per_day)):

    if claims_per_day[i] > threshold:

        # Start of a new run
        if current_run == 0:
            start_day = i

        # Increase current run
        current_run += 1

        # Update longest run
        if current_run > longest_run:

            longest_run = current_run
            best_start_day = start_day

    else:

        # Reset when claims are not above threshold
        current_run = 0


# ------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------

print("=" * 50)
print("INSURANCE CLAIM SPIKE ANALYSIS")
print("=" * 50)

print("\nDaily Claims:")

for day, claims in enumerate(claims_per_day, start=1):
    print(f"Day {day}: {claims} claims")


print("\n" + "-" * 50)

print("Threshold:", threshold)
print("Longest Consecutive Run:", longest_run, "days")

if longest_run > 0:

    end_day = best_start_day + longest_run - 1

    print("Starting Day:", best_start_day + 1)
    print("Ending Day:", end_day + 1)

    print("\nClaims During Longest Run:")

    for i in range(best_start_day, end_day + 1):
        print(f"Day {i + 1}: {claims_per_day[i]} claims")

else:

    print("No claim spike detected.")


print("\n" + "=" * 50)
print("PROGRAM COMPLETED")
print("=" * 50)