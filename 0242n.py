def isAnagram(s, t):
    # If lengths of string s and t are not equal, they can't be anagrams
    if len(s) != len(t):
        return False

    # Create a dictionary to store the character counts
    count = {}

    # Iterate over each character in string s
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in count:
            count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            count[char] = 1

    # Iterate over each character in string t
    for char in t:
        # If the character is not in the dictionary or its count is 0, return False
        if char not in count or count[char] == 0:
            return False
        # If the character is in the dictionary, decrement its count
        else:
            count[char] -= 1

    # If all counts in the dictionary are 0, return True
    return all(value == 0 for value in count.values())
#time O(n)
#space O(1)
