#divide and conquer
def myPow(x, n):
    # If n is 0, x^0 is 1
    if n == 0:
        return 1.0

    # If n is negative, we calculate the reciprocal of x and make n positive
    if n < 0:
        x = 1 / x
        n = -n

    # We initialize the result as 1.0, which will not affect the final multiplication result
    result = 1.0
    current_product = x

    # While n > 0
    while n > 0:
        # If n is odd, we multiply the result by the current product
        if n % 2 == 1:
            result *= current_product
        # We then square the current product
        current_product *= current_product
        # And make n half
        n //= 2

    # Return the final result
    return result
#time O(logn)
#space O(1)
