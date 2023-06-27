#dynamic programming
def canPartition(nums):
    total = sum(nums)
    # If the sum of the elements is odd, return False
    if total % 2 != 0:
        return False

    total = total // 2
    dp = [False] * (total + 1)
    dp[0] = True

    for num in nums:
        for i in range(total, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[total]
#time O(n)
#space O(n)
