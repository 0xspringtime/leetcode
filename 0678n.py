def checkValidString(s):
    # initialize left and right balance to 0
    left = right = 0
    n = len(s)
    
    # iterate from left to right and from right to left simultaneously
    for i in range(n):
        # count '(' and '*' as open on the left side
        if s[i] in '(*':
            left += 1
        else:
            left -= 1
        # count ')' and '*' as open on the right side
        if s[n - i - 1] in ')*':
            right += 1
        else:
            right -= 1
        
        # if balance is negative at any time, it means we have unmatched ')'
        if left < 0 or right < 0:
            return False
    
    # if both balances are non-negative, we have a valid string
    return True
#time O(n)
#space O(1)
