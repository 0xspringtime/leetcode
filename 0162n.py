#binary search
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    # We start by considering the whole array and progressively reduce our search space.
    while left < right:
        mid = (left + right) // 2
        # If mid element is less than next one, peak element is in the right half
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        # If mid element is greater than the next one, peak element is in the left half
        else:
            right = mid
    return left  # or return right, since left == right
#time O(n)
#space O(1)
