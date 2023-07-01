#binary search
def search(nums, target):
    # Initialize two pointers: left and right
    left, right = 0, len(nums) - 1

    # While the left pointer is less than or equal to the right pointer
    while left <= right:
        # Compute the mid index
        mid = (left + right) // 2

        # If the target is found, return its index
        if nums[mid] == target:
            return mid

        # When the middle element is less than the rightmost element,
        # the right half is sorted
        if nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                # Target is in the sorted half
                left = mid + 1
            else:
                # Target is in the other half
                right = mid - 1
        else:
            # The left half is sorted
            if nums[left] <= target < nums[mid]:
                # Target is in the sorted half
                right = mid - 1
            else:
                # Target is in the other half
                left = mid + 1

    # If we have not found the target, return -1
    return -1
#time O(logn)
#space O(1)
