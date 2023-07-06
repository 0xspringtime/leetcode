#sliding window
from collections import Counter

def checkInclusion(s1, s2):
    # Create Counter objects for s1 and the first len(s1) characters in s2
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2[:len(s1)])

    # If the two Counters are equal, return True
    if counter_s1 == counter_s2:
        return True

    # Slide the window over s2
    for i in range(len(s1), len(s2)):
        # Add the new character to the s2 Counter
        counter_s2[s2[i]] += 1
        # Remove the character that was left behind
        counter_s2[s2[i - len(s1)]] -= 1
        if counter_s2[s2[i - len(s1)]] == 0:
            del counter_s2[s2[i - len(s1)]]

        # Compare the two Counters
        if counter_s1 == counter_s2:
            return True

    # If no match is found, return False
    return False
#time O(n)
#space O(1)
