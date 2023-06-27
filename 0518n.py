#dynamic programming
def change(amount, coins):
    # We initialize a list dp with length of amount + 1 and fill it with 0s.
    # dp[i] will be storing the number of solutions for value i.
    # We need amount+1 size because the index is from 0 to amount.
    dp = [0] * (amount + 1)

    # There is exactly 1 way to make 0 - we use 0 coins.
    dp[0] = 1

    # For each coin
    for coin in coins:
        # For each of the amounts from the coin value to the target amount
        for x in range(coin, amount + 1):
            # Update the number of ways we can make that amount by adding the number of ways
            # we can make the current amount - the coin value
            dp[x] += dp[x - coin]

    # The last element in dp is the number of ways we can make the target amount
    return dp[amount]
#time O(n*m)
#space O(m)
