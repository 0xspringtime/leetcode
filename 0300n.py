#dynamic programming
def lengthOfLIS(nums):
    # Edge case: if the list is empty, the length of the longest increasing subsequence is 0
    if not nums:
        return 0

    # Initialize the DP array with 1's
    dp = [1] * len(nums)

    # Iterate over the array
    for i in range(len(nums)):
        # Check all the previous numbers
        for j in range(i):
            # If the current number is greater than a previous number
            if nums[i] > nums[j]:
                # We can extend the increasing subsequence ending at the previous number
                # So, we update the DP value at the current index to be the maximum of what it was and what it would be if we extend the subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the DP array
    return max(dp)
#time O(n^2)
#space O(n)
