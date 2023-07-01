#bits
def singleNumber(nums):
    # initialize result to 0
    result = 0
    
    # iterate over all numbers
    for num in nums:
        # use XOR to find the single number
        result ^= num
    
    return result
#time O(n)
#space O(1)
