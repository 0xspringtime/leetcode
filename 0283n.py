#two pointer
def moveZeroes(nums):
    # Initialize lastNonZeroFoundAt at 0
    lastNonZeroFoundAt = 0

    # Loop through the array
    for i in range(len(nums)):
        # If the current element is not zero
        if nums[i] != 0:
            # Swap the non-zero element with the zero element at lastNonZeroFoundAt
            nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
            # Increment lastNonZeroFoundAt
            lastNonZeroFoundAt += 1
#time O(n)
#space O(1)
