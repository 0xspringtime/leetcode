#dynamic programming
def coinChange(coins, amount):
    # We initialize the DP table with a large value (amount+1)
    # Since the maximum number of coins can be amount (all 1's), amount+1 is out of the possible range
    dp = [amount + 1] * (amount + 1)

    # It takes 0 coins to make 0 amount
    dp[0] = 0

    # We start from the smallest possible amount (1) to the desired amount
    for i in range(1, amount + 1):
        # For each amount, we try each coin
        for coin in coins:
            # We can use the coin only if it's smaller or equal to the current amount
            if coin <= i:
                # We try to subtract the coin and see if it leads to a better result
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the final result is still amount+1, it means we couldn't find any combination to form the amount
    return dp[amount] if dp[amount] != amount + 1 else -1
#time O(n)
#space O(1)
