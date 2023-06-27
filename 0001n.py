#dictionary
def twoSum(nums, target):
    # Initialize an empty dictionary
    seen = {}

    # Iterate through the list of numbers with their indices
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num

        # If the complement is in the dictionary, we have found the two numbers
        if complement in seen:
            return [seen[complement], i]

        # If not, add the current number and its index to the dictionary
        seen[num] = i
#time O(n)
#space O(n)
