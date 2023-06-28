#two pointer
#sorting
def threeSum(nums):
    # Sort the array in ascending order
    nums.sort()

    result = []

    # Iterate over the array
    for i in range(len(nums) - 2):
        # Skip if the current value is the same as the previous one to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize two pointers, one at the current index + 1, and the other at the end of the array
        left, right = i + 1, len(nums) - 1

        # While the left pointer is less than the right pointer
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                # If total is less than 0, we need to increase the sum, so we move the left pointer to the right
                left += 1
            elif total > 0:
                # If total is more than 0, we need to decrease the sum, so we move the right pointer to the left
                right -= 1
            else:
                # If total is 0, we found a triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates from the left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates from the right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers towards the center
                left += 1
                right -= 1

    return result
#time O(n^2)
#space O(n)
