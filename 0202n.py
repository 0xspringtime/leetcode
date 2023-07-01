def isHappy(n):
    # Create a set to store the sums we have seen before
    seen = set()
    
    while n != 1 and n not in seen:
        # Add the current number to the set
        seen.add(n)
        # Compute the sum of the squares of the digits
        n = sum(int(digit)**2 for digit in str(n))
        
    # If we reach 1, then n is a happy number
    return n == 1
#time O(logn)
#space O(logn)
