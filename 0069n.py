#binary search
def mySqrt(x):
    # If x is less than 2, return x
    if x < 2:
        return x

    # Define the left and right boundaries for binary search
    left, right = 1, x // 2

    # Start the binary search
    while left <= right:
        # Calculate the mid value
        mid = left + (right - left) // 2
        # If the square of mid is less than x
        if mid * mid < x:
            # Move the left boundary to mid + 1
            left = mid + 1
        # If the square of mid is greater than x
        elif mid * mid > x:
            # Move the right boundary to mid - 1
            right = mid - 1
        # If the square of mid is equal to x
        else:
            return mid

    # If we can't find an exact square root, we return the right boundary (as we are rounding down)
    return right
#time O(logn)
#space O(1)
