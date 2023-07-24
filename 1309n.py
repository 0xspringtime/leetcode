def freqAlphabets(s):
    # Define the mapping from digits to characters
    mapping = [str(i) for i in range(1, 10)] + [str(i)+'#' for i in range(10, 27)]
    characters = list('abcdefghijklmnopqrstuvwxyz')
    digit_to_char = dict(zip(mapping, characters))

    # Initialize the result string
    result = ''

    # Scan the string from right to left
    i = len(s) - 1
    while i >= 0:
        if s[i] == '#':
            # The current character is '#', so the previous two characters form a number
            number = s[i-2:i+1]
            i -= 3
        else:
            # The current character is a digit
            number = s[i]
            i -= 1

        # Map the number to a character and append it to the result string
        result += digit_to_char[number]

    # Reverse the result string to get the answer in the correct order
    return result[::-1]
#time O(n)
#space O(n)
