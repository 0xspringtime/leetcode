#bits
def hammingDistance(x, y):
    # Perform XOR operation on x and y
    xor = x ^ y

    # Convert the result to binary and count the number of '1's
    return bin(xor).count('1')
#time O(1)
#space O(1)
