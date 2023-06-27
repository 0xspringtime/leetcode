#DFS
def generateParenthesis(n):
    # Initialize an empty list to store the results
    res = []

    # Recursive helper function to generate parenthesis
    def helper(S, left, right):
        # If we reach the end, append the string to the result list
        if len(S) == 2 * n:
            res.append(''.join(S))
            return
        # If we have left opening brackets, add an opening bracket
        if left < n:
            S.append('(')
            helper(S, left + 1, right)
            S.pop()
        # If we have left closing brackets, add a closing bracket
        if right < left:
            S.append(')')
            helper(S, left, right + 1)
            S.pop()

    # Call the helper function with an empty string and 0 left and right brackets
    helper([], 0, 0)

    # Return the final list of well-formed parentheses
    return res
#time O(4^n / sqrt(n)) 
#space O(n)
