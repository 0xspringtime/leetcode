#two pointer
def partitionDisjoint(nums):
    # Initialize max_left and max_here to the first number in the list
    max_left = max_here = nums[0]
    # Initialize the partition index to 0
    partition_idx = 0

    # Loop over the list from index 1 to the end
    for i in range(1, len(nums)):
        # If the current number is less than max_left, update the partition index
        # and set max_left to max_here
        if nums[i] < max_left:
            max_left = max_here
            partition_idx = i
        # Otherwise, update max_here if the current number is greater than max_here
        elif nums[i] > max_here:
            max_here = nums[i]

    # The length of the left partition is one more than the partition index
    # because list indices are 0-based
    return partition_idx + 1
#time O(n)
#space O(1)
