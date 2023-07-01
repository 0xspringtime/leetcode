#bits
def divide(dividend, divisor):
    # Handling the case of overflow
    MAX_INT = 2147483647        # 2**31 - 1
    if dividend == -2147483648 and divisor == -1:
        return MAX_INT

    # Checking if the result is negative
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    quotient = 0
    # While the dividend is less than or equal to the divisor
    while dividend <= divisor:
        # Start from power of 1
        power_of_two = 1
        value = divisor
        # Try to "double" the current value and power_of_two
        while value >= -1073741824 and value + value >= dividend:
            value += value;
            power_of_two += power_of_two
        # Update quotient and dividend
        quotient += power_of_two
        dividend -= value

    # If there was originally one negative sign, then quotient remains negative.
    # Otherwise, negate quotient to make it positive.
    return -quotient if negatives != 1 else quotient
#time O(logn)
#space O(1)
