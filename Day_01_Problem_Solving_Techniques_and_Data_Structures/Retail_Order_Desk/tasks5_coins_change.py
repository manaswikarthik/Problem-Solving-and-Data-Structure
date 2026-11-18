# ==========================================
# TASK 5 - COIN CHANGE
# GREEDY vs DYNAMIC PROGRAMMING
# ==========================================

import time


# ------------------------------------------
# 1. GREEDY ALGORITHM
# ------------------------------------------

def greedy_coin_change(amount, denominations):
    coins_used = []

    for coin in denominations:
        while amount >= coin:
            amount -= coin
            coins_used.append(coin)

    return coins_used


# ------------------------------------------
# 2. DYNAMIC PROGRAMMING
# ------------------------------------------

def dp_coin_change(amount, denominations):

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)

    for current_amount in range(1, amount + 1):

        for coin in denominations:

            if coin <= current_amount:

                if dp[current_amount - coin] + 1 < dp[current_amount]:

                    dp[current_amount] = dp[current_amount - coin] + 1
                    coin_used[current_amount] = coin

    # Reconstruct solution
    result = []
    current_amount = amount

    while current_amount > 0:

        coin = coin_used[current_amount]
        result.append(coin)
        current_amount -= coin

    return result


# ------------------------------------------
# 3. MAIN PROGRAM
# ------------------------------------------

print("=" * 60)
print("          REFUND COIN CHANGE SYSTEM")
print("=" * 60)


# Indian currency denominations
denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]

refund_amount = 786


# ------------------------------------------
# 4. GREEDY APPROACH
# ------------------------------------------

start = time.perf_counter()

greedy_result = greedy_coin_change(
    refund_amount,
    denominations
)

greedy_time = time.perf_counter() - start


print("\n--- Greedy Algorithm ---")

print("Refund Amount:", refund_amount)
print("Coins/Notes Used:", greedy_result)
print("Total Notes/Coins:", len(greedy_result))
print(f"Execution Time: {greedy_time:.8f} seconds")


# ------------------------------------------
# 5. DYNAMIC PROGRAMMING
# ------------------------------------------

start = time.perf_counter()

dp_result = dp_coin_change(
    refund_amount,
    denominations
)

dp_time = time.perf_counter() - start


print("\n--- Dynamic Programming ---")

print("Refund Amount:", refund_amount)
print("Coins/Notes Used:", dp_result)
print("Total Notes/Coins:", len(dp_result))
print(f"Execution Time: {dp_time:.8f} seconds")


# ------------------------------------------
# 6. GREEDY FAILURE EXAMPLE
# ------------------------------------------

print("\n--- Example Where Greedy Fails ---")

test_denominations = [4, 3, 1]
test_amount = 6

greedy_failure = greedy_coin_change(
    test_amount,
    test_denominations
)

dp_solution = dp_coin_change(
    test_amount,
    test_denominations
)

print("Denominations:", test_denominations)
print("Amount:", test_amount)

print("\nGreedy Solution:", greedy_failure)
print("Number of Coins:", len(greedy_failure))

print("\nDP Solution:", dp_solution)
print("Number of Coins:", len(dp_solution))


# ------------------------------------------
# 7. COMPARISON
# ------------------------------------------

print("\n--- Comparison ---")

print("Greedy:", len(greedy_result), "coins/notes")
print("Dynamic Programming:", len(dp_result), "coins/notes")

print("=" * 60)