#dynamic programming
def rob(nums):
    # If the list of houses is empty, return 0
    if not nums:
        return 0
    # If there is only one house, return its value
    if len(nums) == 1:
        return nums[0]

    # Helper function to calculate the max money can rob given a start and end index
    def rob_range(start, end):
        rob_next_plus_one = 0
        rob_next = 0
        for i in range(end, start - 1, -1):
            current = max(rob_next, rob_next_plus_one + nums[i])
            rob_next_plus_one = rob_next
            rob_next = current
        return rob_next

    # Calculate the maximum robbery for two scenarios and return the maximum of them
    return max(rob_range(0, len(nums) - 2), rob_range(1, len(nums) - 1))
#time O(n)
#space O(1)
