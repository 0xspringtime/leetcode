def countSubstrings(s):
    # Initialize count to 0
    count = 0
    # Iterate over all substrings of s
    for center in range(2*len(s) - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count
#time O(n^2)
#space O(1)
