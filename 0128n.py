#hash set
def longestConsecutive(nums):
    # Convert the list into a set for efficient lookup
    nums = set(nums)

    # Initialize the length of the longest consecutive elements sequence
    longest_sequence = 0

    # Iterate over the set
    for num in nums:
        # If the current number is the start of a sequence, try to extend the sequence
        if num - 1 not in nums:
            current_num = num
            current_sequence = 1

            # Extend the sequence as far as possible
            while current_num + 1 in nums:
                current_num += 1
                current_sequence += 1

            # Update the length of the longest consecutive elements sequence
            longest_sequence = max(longest_sequence, current_sequence)

    # Return the length of the longest consecutive elements sequence
    return longest_sequence
#time O(n)
#space O(n)
