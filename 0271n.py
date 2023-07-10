def encode(strs):
    # For each string, we store its length followed by a special character (like ':') followed by the string itself
    return ''.join('%d:%s' % (len(s), s) for s in strs)

def decode(s):
    strs = []
    i = 0
    while i < len(s):
        # We find the index of the special character ':'
        j = s.find(':', i)
        # We get the length of the string which was stored before the special character
        length = int(s[i:j])
        # We get the string of that length after the special character
        strs.append(s[j + 1:j + 1 + length])
        # Move the index to the next string
        i = j + 1 + length
    return strs
#time O(n)
#space O(n)
