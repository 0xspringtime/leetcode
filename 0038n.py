def countAndSay(n):
    # base case
    if n == 1:
        return "1"

    # get the (n-1)th term
    prev_term = countAndSay(n - 1)
    
    # variables to hold the count of current digit and the result string
    count = 0
    result = ''
    
    # initialize the current character
    current_char = prev_term[0]
    
    for char in prev_term:
        if char == current_char:
            count += 1 # increment count if the character is same as current_char
        else:
            result += str(count) + current_char # append count and current character to the result
            current_char = char # update current character
            count = 1 # reset count
    
    # append the count and character for the last group
    result += str(count) + current_char
    
    return result
#time O(2^n)
#space O(2^n)
