def largestNumber(nums):
    # Convert the integers to strings for comparison
    nums = list(map(str, nums))
    
    # Custom comparison function
    nums.sort(key = lambda x, y: cmp(y + x, x + y))
    
    # Joining the sorted numbers
    largest = ''.join(nums)
    
    # Handling the leading zeros case
    return '0' if largest[0] == '0' else largest

# Custom comparator for sorting
def cmp(a, b):
    return (a > b) - (a < b) 
#time O(nlogn)
#space O(n)
