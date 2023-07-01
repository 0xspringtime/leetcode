def groupAnagrams(strs):
    # Create an empty dictionary to store the sorted version of word as key and their anagrams as values
    anagrams = {}

    # Loop through each word in the given list
    for word in strs:
        # Sort the word and convert it back to a string
        sorted_word = "".join(sorted(word))

        # Check if sorted_word is already a key in the dictionary
        if sorted_word in anagrams:
            # If it is, append the original word to the list of its anagrams
            anagrams[sorted_word].append(word)
        else:
            # If it's not, add a new entry in the dictionary with the sorted word as the key 
            # and a new list containing the original word as its value
            anagrams[sorted_word] = [word]
            
    # Return the anagram groups
    return list(anagrams.values())
#time O(nmlogn)
#space O(nm)
