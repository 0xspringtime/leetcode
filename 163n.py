def findMissingRanges(nums, lower, upper):
    def formatRange(lower, upper):
        if lower == upper:
            return str(lower)
        else:
            return str(lower) + "->" + str(upper)
        
    results = []
    nums = [lower - 1] + nums + [upper + 1]  # add two dummy elements

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:  # there is a missing range
            results.append(formatRange(nums[i - 1] + 1, nums[i] - 1))
    
    return results
#time O(n)
#space O(n)
