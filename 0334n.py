def increasingTriplet(nums):
    # initialize first minimum and second minimum to the maximum possible number
    first_min = second_min = float('inf')
    # iterate over the list
    for num in nums:
        # if this number is smaller than first_min, update first_min
        if num <= first_min:
            first_min = num
        # if this number is between first_min and second_min, update second_min
        elif num <= second_min:
            second_min = num
        # if this number is bigger than both, we found a triplet
        else:
            return True
    # if no such triplet found, return False
    return False
#time O(n)
#space O(1)
