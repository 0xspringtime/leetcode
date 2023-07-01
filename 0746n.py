#dynamic programming
def minCostClimbingStairs(cost):
    n = len(cost)
    # Initialize dp array with size n+1 to account for the "top of the floor"
    dp = [0] * (n + 1)
    # Base cases, either start from step 0 or step 1
    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, n + 1):
        # If we are at the top of the floor, we do not need to pay any cost
        cost_i = 0 if i == n else cost[i]
        # The minimum cost to reach i-th step would be the cost to reach the i-th step plus
        # the minimum cost to reach (i-1)th step or (i-2)th step.
        dp[i] = cost_i + min(dp[i - 1], dp[i - 2])

    # Return the minimum cost to reach the top of the floor
    return dp[n]
#time O(n)
#space O(n)
