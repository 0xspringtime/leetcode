def addToArrayForm(num, k):
    # Convert the list of digits into an integer
    num_as_int = int(''.join(map(str, num)))

    # Add k to the number
    total = num_as_int + k

    # Convert the sum back into a list of digits
    total_as_array = [int(digit) for digit in str(total)]

    return total_as_array
#time O(n)
#space O(n)
