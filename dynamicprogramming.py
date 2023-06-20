def knapsack(values, weights, capacity):
    n = len(values)
    
    # Create a DP table of size (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    # Fill up the DP table
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                # Choose the maximum value between not taking or taking the item i
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]  # Don't take the item i

    # The bottom-right corner of the DP table contains the maximum value
    return dp[-1][-1]

#Identify the problem structure: Problems that require DP usually ask for an optimization over a sequence and have overlapping subproblems. These properties are common in many classic DP problems, such as Knapsack, Longest Common Subsequence, and Matrix Chain Multiplication.

#Define the state: DP problems involve different states that you transition between. A state is a way to represent a subproblem. For instance, in the 0/1 Knapsack problem, the states can be represented as a 2D array dp[i][j] where each state dp[i][j] represents the maximum value we can accumulate with i items and a capacity of j.

#Formulate a recurrence relation: A recurrence relation is an equation that expresses the solution of a problem in terms of smaller sub-problems. In the case of the 0/1 Knapsack problem, the recurrence relation can be defined as follows:
#dp[i][j] = max(dp[i-1][j], values[i] + dp[i-1][j-weights[i]]) if weights[i] <= j else dp[i-1][j]

#Define the base case and initialize the DP table: The base case in the DP is usually straightforward and occurs when the problem is minimized to an extent where the answer is trivial. In the 0/1 Knapsack problem, the base case is when there are no items or the capacity is 0, in which case, the value accumulated is 0.
