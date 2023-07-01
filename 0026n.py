#two pointer
def removeDuplicates(nums):
    # If the list is empty, return 0
    if not nums:
        return 0

    # Initialize the first pointer at the second element (index 1)
    i = 1

    # Initialize the second pointer at the first element (index 0)
    j = 0

    # While we have not reached the end of the list
    while i < len(nums):
        # If the current element is different from the previous one
        if nums[i] != nums[j]:
            # Move the second pointer one step forward
            j += 1
            # Copy the current element to the position of the second pointer
            nums[j] = nums[i]
        # Move the first pointer one step forward
        i += 1

    # Return the number of unique elements
    return j + 1
#time O(n)
#space O(1)
