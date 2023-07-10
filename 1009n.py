def findComplement(n: int) -> int:
    # Find the number of bits in the given integer
    num_of_bits = n.bit_length()

    # Generate a number of all ones which is of the same length as n
    all_ones = (1 << num_of_bits) - 1

    # Return the bitwise complement of the number
    return n ^ all_ones
#time O(1)
#space O(1)
