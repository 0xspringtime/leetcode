#dynamic programming
def findTargetSumWays(nums, target):
    dp = {0: 1}
    for num in nums:
        new_dp = {}
        for sum, count in dp.items():
            new_dp[sum + num] = new_dp.get(sum + num, 0) + count
            new_dp[sum - num] = new_dp.get(sum - num, 0) + count
        dp = new_dp
    return dp.get(target, 0)
#time O(n*sum)
#space O(sum)
