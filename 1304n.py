def sumZero(n):
    # Generate numbers from -n//2 to n//2. Exclude zero if n is even.
    result = list(range(-n//2, n//2 + 1))
    #include 0 if n is odd
    if n % 2 == 0:
        result.remove(0)
    return result
#time O(n)
#space O(n)
