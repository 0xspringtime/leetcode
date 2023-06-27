#two pointer
def twoSum(numbers, target):
    # Initialize two pointers, one at the start of the array and one at the end
    left, right = 0, len(numbers) - 1

    while left < right:
        # Calculate the current sum
        current_sum = numbers[left] + numbers[right]

        # If the current sum is equal to the target, return the indices (1-indexed)
        if current_sum == target:
            return [left + 1, right + 1]

        # If the current sum is less than the target, move the left pointer to the right
        elif current_sum < target:
            left += 1

        # If the current sum is greater than the target, move the right pointer to the left
        else:
            right -= 1

#time O(n)
#space O(1)
