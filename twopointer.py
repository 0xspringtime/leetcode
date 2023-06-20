def two_sum(sorted_nums, target):
    # Initialize two pointers
    left, right = 0, len(sorted_nums) - 1

    while left < right:
        current_sum = sorted_nums[left] + sorted_nums[right]

        # If the current sum equals the target, we found our pair
        if current_sum == target:
            return [sorted_nums[left], sorted_nums[right]]
        # If the current sum is less than the target, we move the left pointer to the right
        elif current_sum < target:
            left += 1
        # If the current sum is greater than the target, we move the right pointer to the left
        else:
            right -= 1

    # Return an indication that no pair was found
    return [-1, -1]

The two-pointer technique is a very useful strategy that can be used in solving a variety of array/string problems especially those that ask for a pair of elements that satisfy certain conditions.

The idea behind the two-pointer technique is that you have two pointers, usually one at the beginning and one at the end of the array/string, and you move them based on the condition that you are trying to satisfy.

#Note that this works on a sorted array. If the array was not sorted, we'd have to sort it first which would add to the time complexity.

#In this problem, we're using the property of the sorted array to decide whether to move the left pointer or the right pointer. If the sum is too small, we know that moving the right pointer to the left would only make the sum smaller, so we have to move the left pointer to the right. Conversely, if the sum is too large, we move the right pointer to the left.

#The time complexity of the two-pointer approach is typically O(n), since each element is visited at most once by either the left or the right pointer. This makes it a very efficient strategy for solving these types of problems.


