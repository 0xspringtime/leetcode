#dynamic programming
def maxProduct(nums):
    # Initialize the variables
    maxProd = minProd = res = nums[0]

    # Iterate over the array starting from the second element
    for num in nums[1:]:
        # If the current number is negative, swapping the max and min product will be beneficial
        if num < 0:
            maxProd, minProd = minProd, maxProd

        # We either take the current number as the start of a new subarray, or include it in an existing subarray
        maxProd = max(num, maxProd * num)
        minProd = min(num, minProd * num)

        # Update the result with the maximum product
        res = max(res, maxProd)

    return res
#time O(n)
#space O(1)
