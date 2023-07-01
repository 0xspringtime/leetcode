#greedy
def canJump(nums):
    # Start from the end of the array
    target = len(nums) - 1

    # Move backwards through the array
    for i in range(len(nums)-2, -1, -1):
        # If the current position can jump to or past the target
        if i + nums[i] >= target:
            # Update the target to the current position
            target = i

    # Return whether we have reached the start
    return target == 0
#time O(n)
#space O(1)
