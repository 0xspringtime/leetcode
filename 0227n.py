#stack
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    num = 0
    sign = '+'

    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            else:
                stack[-1] = int(stack[-1] / num)  # note: python 2.x int division trancates toward negative infinity
            num = 0
            sign = s[i]

    return sum(stack)
#time O(n)
#space O(n)
