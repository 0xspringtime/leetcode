#sliding window
def findRepeatedDnaSequences(s):
    # We will use the Python collections library to create a Counter, which is a dictionary subclass
    from collections import Counter

    # Initialize a counter for all 10-letter-long sequences in s
    sequences = Counter([s[i:i+10] for i in range(len(s)-9)])

    # Select the keys of sequences which have values greater than 1
    # These are the sequences which appear more than once
    repeated_sequences = [sequence for sequence, count in sequences.items() if count > 1]

    return repeated_sequences
#time O(n)
#space O(n)
