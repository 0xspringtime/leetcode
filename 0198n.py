#dynamic programming
def rob(nums):
    # If the list of houses is empty, return 0
    if not nums:
        return 0

    # If there is only one house, return the amount of money in it
    if len(nums) == 1:
        return nums[0]

    # Create a list to store the maximum amount of money that can be robbed up to each house
    dp = [0]*len(nums)

    # Initialize the list with the amount of money in the first house and the maximum of the first two houses
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Iterate over the rest of the houses
    for i in range(2, len(nums)):
        # Update the maximum amount of money that can be robbed up to the current house
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    # Return the maximum amount of money that can be robbed from all houses
    return dp[-1]
#time O(n)
#space O(n)
