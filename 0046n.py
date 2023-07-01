#backtracking
def permute(nums):
    """
    This function receives a list of numbers and returns a list of lists
    containing all possible permutations of the numbers.
    """

    # The final list of permutations
    results = []

    # A helper function to perform the permutations using backtracking
    def backtrack(perm, nums):
        # If there are no more numbers to add, the permutation is complete
        if not nums:
            results.append(perm)
            return
        # Go through the remaining numbers
        for i in range(len(nums)):
            # Make a new permutation by adding the current number
            # Remove the number from the remaining pool
            backtrack(perm + [nums[i]], nums[:i] + nums[i+1:])

    # Start the backtracking with an empty permutation
    backtrack([], nums)

    return results
#time O(n*n!)
#space O(n*n!)
