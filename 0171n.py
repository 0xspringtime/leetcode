def titleToNumber(columnTitle):
    result = 0

    # Iterate over each character in reverse order
    for i in range(len(columnTitle) - 1, -1, -1):
        # Get the numeric value of the current character
        value = ord(columnTitle[i]) - ord('A') + 1

        # Multiply the value by the corresponding power of 26 and add it to the result
        result += value * (26 ** (len(columnTitle) - i - 1))

    return result
#time O(n)
#space O(1)
