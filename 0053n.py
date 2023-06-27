#kadane
#dynamic programming
def maxSubArray(nums):
    """
    This function receives a list of numbers and returns the sum of the subarray
    with the largest sum in the list.
    """

    # Initialize current_sum and max_sum with the first element of the list.
    current_sum = max_sum = nums[0]

    # Iterate over the rest of the list
    for num in nums[1:]:
        # Update current_sum:
        #   if current_sum is negative, discard it and start a new subarray.
        #   if current_sum is non-negative, extend the current subarray.
        current_sum = max(num, current_sum + num)
        # Update max_sum if necessary
        max_sum = max(max_sum, current_sum)

    return max_sum

#time O(n)
#space O(1)
