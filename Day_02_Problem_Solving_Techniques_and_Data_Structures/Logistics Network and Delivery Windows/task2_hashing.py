# Logistics Network and Delivery Windows
# Task 2: Hash Map for Parcel Tracking
# Detect Duplicate Scans at the Same Hub

# Hash map to store parcel tracking information
parcels = {}

# Scan parcel at a hub
def scan_parcel(tracking_number, hub_code):

    # Create entry if parcel is not already present
    if tracking_number not in parcels:
        parcels[tracking_number] = []

    # Check if parcel was already scanned at this hub
    if hub_code in parcels[tracking_number]:
        print(f"Duplicate Scan Detected!")
        print(f"Parcel: {tracking_number}")
        print(f"Hub: {hub_code}")

    else:
        parcels[tracking_number].append(hub_code)
        print(f"Scan Recorded: Parcel {tracking_number} at Hub {hub_code}")


# -----------------------------------
# Main Program
# -----------------------------------

print("=" * 50)
print("LOGISTICS NETWORK MANAGEMENT")
print("TASK 2: PARCEL TRACKING USING HASH MAP")
print("=" * 50)

# Parcel scanning operations
scan_parcel("TRK101", "CHN01")
scan_parcel("TRK102", "BLR01")
scan_parcel("TRK101", "CHN02")
scan_parcel("TRK101", "CHN01")
scan_parcel("TRK102", "BLR01")
scan_parcel("TRK103", "HYD01")
scan_parcel("TRK103", "HYD02")

# -----------------------------------
# Display Parcel Records
# -----------------------------------

print("\n" + "-" * 50)
print("PARCEL TRACKING RECORDS")
print("-" * 50)

for tracking_number, hubs in parcels.items():
    print(f"{tracking_number} -> {hubs}")

# -----------------------------------
# Search Parcel
# -----------------------------------

print("\n" + "-" * 50)
print("PARCEL SEARCH")

search_tracking = "TRK101"

if search_tracking in parcels:
    print(f"{search_tracking} found.")
    print(f"Scanned at hubs: {parcels[search_tracking]}")
else:
    print(f"{search_tracking} not found.")

# -----------------------------------
# Test Cases
# -----------------------------------

print("\n" + "-" * 50)
print("TEST CASES")
print("-" * 50)

# New parcel
scan_parcel("TRK200", "MUM01")

# Same parcel at a different hub
scan_parcel("TRK200", "DEL01")

# Duplicate scan at same hub
scan_parcel("TRK200", "MUM01")

print("\n" + "=" * 50)
print("PROGRAM COMPLETED")
print("=" * 50)