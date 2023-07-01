#dynamic programming
def combinationSum4(nums, target):
    # Initialize the dp list
    dp = [0] * (target + 1)
    dp[0] = 1  # There is one way to make a sum of 0

    # For each number in nums
    for num in nums:
        # For each value from num to target
        for i in range(num, target + 1):
            # Add the number of combinations that add up to i - num
            dp[i] += dp[i - num]
    # Return the number of combinations that add up to target
    return dp[target]
#time O(k*n)
#space O(k)
