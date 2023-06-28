#bits
def reverseBits(n):
    # Initialize the result to 0
    result = 0

    # Traverse through all bits of the input number
    for _ in range(32):  # as we are working with 32 bit numbers
        # Shift the bits of the result to the left
        result <<= 1

        # Add the last bit of the input number to the result
        result |= n & 1  # 'n & 1' gives us the last bit of 'n'

        # Shift the bits of the input number to the right
        n >>= 1

    return result
#time O(1)
#space O(1)
