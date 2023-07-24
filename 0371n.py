def getSum(a, b):
    # Constants for 32-bit overflow
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    mask = 0xFFFFFFFF

    while b != 0:
        # Carry now contains common set bits of a and b
        carry = ((a & b) & mask)

        # Sum of bits of a and b where at least one of the bits is not set
        a = (a ^ b) & mask

        # Carry is shifted by one so that adding it to a gives the required sum
        b = (carry << 1) & mask

    # If a is negative, convert it to its equivalent positive number
    if a <= MAX:
        return a
    # If a is positive, return its negative equivalent
    else:
        return ~(a ^ mask)
#time O(1)
#space O(1)
