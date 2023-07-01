#backtrack
def subsetsWithDup(nums):
    # Sort the numbers to handle duplicates
    nums.sort()

    # List to hold the final results
    results = []

    # Kick off the backtracking process
    backtrack(nums, 0, [], results)

    return results

def backtrack(nums, index, path, results):
    # Add the current path to the results
    results.append(path)

    for i in range(index, len(nums)):
        # If the current number is same as the previous number, skip it to avoid duplicates
        if i > index and nums[i] == nums[i-1]:
            continue

        # Call the function recursively with the next index and current path appended with the current number
        backtrack(nums, i+1, path+[nums[i]], results)
#time O(n * 2^n)
#space O(n * 2^n)
