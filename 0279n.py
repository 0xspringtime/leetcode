#dynamic programming
def numSquares(n):
    # Step 1: Initialize dp array
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Step 2: Fill up the dp array
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    # Step 3: Return the result
    return dp[n]
#time O(n*sqrt(n))
#space O(n)
