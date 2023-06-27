#binary search
def findMin(nums):
    # Initialize left and right pointers
    left, right = 0, len(nums) - 1

    # While left pointer is less than right pointer
    while left < right:
        # Calculate the middle index
        mid = (left + right) // 2

        # If the middle element is greater than the rightmost element,
        # then the minimum element must be in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        # Else the minimum element is in the left half
        else:
            right = mid

    # Return the minimum element
    return nums[left]
#time O(logn)
#space O(1)
