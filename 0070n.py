#dynamic programming
def climbStairs(n):
    # If n is less than or equal to 2, then the number of ways is equal to n itself
    if n <= 2:
        return n

    # Create a list to store the number of ways for each step
    dp = [0]*(n+1)

    # There's 1 way to reach the 1st step and 2 ways to reach the 2nd step
    dp[1] = 1
    dp[2] = 2

    # Start from the 3rd step and fill up the dp list using the formula:
    # dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]  # Return the number of ways to reach the nth step
#time O(n)
#space O(n)
