#bits
def hammingWeight(n):
    # Convert the integer to binary and remove the '0b' prefix.
    binary = bin(n)[2:]

    # Count and return the number of '1' bits.
    return binary.count('1')
#time O(1)
#space O(1)
