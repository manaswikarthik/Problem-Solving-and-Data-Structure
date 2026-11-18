# Insurance Claims Management
# Task 2: Duplicate Claim Detection Using Hashing


# Sample claims
claims = [
    ("POL123", "2026-11-10"),
    ("POL456", "2026-11-12"),
    ("pol123", "2026-11-10"),
    ("POL 456", "2026-11-12"),
    ("POL789", "2026-11-15"),
    ("POL999", "2026-11-18"),
    ("pol999", "2026-11-18")
]


# Hash set to store previously seen claims
seen_claims = set()


# Function to normalize policy numbers
def normalize_policy(policy):

    return policy.replace(" ", "").lower()


# Detect duplicate claims
print("CLAIM DUPLICATE DETECTION")
print("-" * 35)

for policy, incident_date in claims:

    # Normalize policy number
    normalized_policy = normalize_policy(policy)

    # Create a unique key
    claim_key = (normalized_policy, incident_date)

    # Check whether the claim already exists
    if claim_key in seen_claims:

        print("Duplicate Claim:", policy, incident_date)

    else:

        seen_claims.add(claim_key)

        print("New Claim:", policy, incident_date)


print("\nTotal Claims:", len(claims))
print("Unique Claims:", len(seen_claims))
print("Duplicate Claims:", len(claims) - len(seen_claims))