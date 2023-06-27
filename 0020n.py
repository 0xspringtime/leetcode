#stack
def isValid(s):
    # This dictionary represents the pairings of the brackets
    bracket_dict = {')': '(', ']': '[', '}': '{'}

    # Initialize a stack to hold the brackets
    stack = []

    # Iterate over each character in the string
    for char in s:
        # If the character is an open bracket, add it to the stack
        if char in bracket_dict.values():
            stack.append(char)
        # If the character is a closed bracket, check if the stack is not empty and the top of the stack is the corresponding open bracket
        elif stack and bracket_dict[char] == stack[-1]:
            # If it is, pop the open bracket from the stack
            stack.pop()
        else:
            # If the stack is empty or the top of the stack isn't the corresponding open bracket, return False
            return False

    # If the stack is empty at the end, return True, else return False
    return not stack
#time O(n)
#space O(n)
