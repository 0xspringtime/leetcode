def isPalindrome(x: int) -> bool:
    # negative numbers cannot be palindrome because of '-'
    if x < 0:
        return False

    # Converting the integer to string
    x_str = str(x)

    # Checking if the string is the same as its reverse.
    return x_str == x_str[::-1]
#time O(n)
#space O(n)
