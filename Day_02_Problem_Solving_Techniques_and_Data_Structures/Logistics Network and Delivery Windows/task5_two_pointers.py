# Logistics Network and Delivery Windows
# Task 5: Palindrome Route Checker
# Algorithm: Two Pointers

def is_palindrome_route(route):

    # Normalize route
    route = route.lower()

    # Remove separators
    route = route.replace("-", "")
    route = route.replace(" ", "")
    route = route.replace(",", "")
    route = route.replace("_", "")

    # Two pointers
    left = 0
    right = len(route) - 1

    while left < right:

        if route[left] != route[right]:
            return False

        left += 1
        right -= 1

    return True


# -----------------------------------
# Main Program
# -----------------------------------

print("=" * 55)
print("LOGISTICS NETWORK MANAGEMENT")
print("TASK 5: PALINDROME ROUTE CHECKER")
print("=" * 55)

routes = [
    "CHN-BLR-CHN",
    "CHN-BLR-HYD",
    "CHN, BLR, CHN",
    "chn-blr-chn",
    "DEL-MUM-BLR-MUM-DEL"
]

for route in routes:

    result = is_palindrome_route(route)

    print(f"\nRoute: {route}")

    if result:
        print("Result: Palindrome Route")
    else:
        print("Result: Not a Palindrome Route")


# -----------------------------------
# Test Cases
# -----------------------------------

print("\n" + "-" * 55)
print("TEST CASES")
print("-" * 55)

# Test Case 1: Palindrome
print("\nTest Case 1:")
print(is_palindrome_route("CHN-BLR-CHN"))

# Test Case 2: Not palindrome
print("\nTest Case 2:")
print(is_palindrome_route("CHN-BLR-HYD"))

# Test Case 3: Different casing
print("\nTest Case 3:")
print(is_palindrome_route("chn-BLR-chn"))

# Test Case 4: Spaces and separators
print("\nTest Case 4:")
print(is_palindrome_route("CHN, BLR, CHN"))

# Test Case 5: Empty route
print("\nTest Case 5:")
print(is_palindrome_route(""))

# Test Case 6: Single character
print("\nTest Case 6:")
print(is_palindrome_route("A"))

print("\n" + "=" * 55)
print("PROGRAM COMPLETED")
print("=" * 55)