#backtracking
def subsets(nums):
    # Initialize the result with the empty set
    result = [[]]

    # Loop over the numbers
    for num in nums:
     # For each number, add it to all existing subsets to form new subsets
        result += [curr + [num] for curr in result]

    # Return the result
    return result
#time O(n*2^n)
#space O(n*2^n)
