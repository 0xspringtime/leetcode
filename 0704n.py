#binary search
def search(nums, target):
    # Set initial left and right pointers
    left, right = 0, len(nums) - 1

    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2

        # If the target is the middle element, return the index
        if nums[mid] == target:
            return mid

        # If target is less than the middle element, discard the right half
        elif nums[mid] > target:
            right = mid - 1

        # If target is greater than the middle element, discard the left half
        else:
            left = mid + 1

    # If we've reached here, it means the target is not in the array
    return -1

#time O(logn)
#space O(1)

# Example usage:
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
print(search(nums1, target1))  # Output: 4

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
print(search(nums2, target2))  # Output: -1
