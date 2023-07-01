def reverse(x):
    # This variable will hold the reversed number
    rev = 0

    # Check if the number is negative
    is_negative = x < 0

    # If negative, make it positive for simplicity
    if is_negative:
        x = -x

    while x != 0:
        # Pop the last digit from x
        pop = x % 10
        x //= 10

        # Check if the reversed number will be out of the 32-bit signed integer range after the next step
        if rev > 214748364 or (rev == 214748364 and pop > 7):
            return 0

        # Push the popped digit to rev
        rev = rev * 10 + pop

    # If x was negative, then the reversed number should also be negative
    return -rev if is_negative else rev
#time O(log(x))
#space O(1)
