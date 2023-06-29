def missingNumber(nums):
    # Calculate the length of nums
    n = len(nums)
    
    # Compute the sum of the first n natural numbers using the formula
    total = n*(n+1)//2
    
    # Subtract the sum of numbers in nums from total to get the missing number
    missing_number = total - sum(nums)
    
    return missing_number
#time O(n)
#space O(1)
