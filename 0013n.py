def roman_to_int(s):
    # Step 1: Create a dictionary to map Roman numerals to integer values
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Step 2: Initialize a variable to store the total
    total = 0

    # Step 3: Loop through the Roman numeral string
    for i in range(len(s)):
        # Add the current value to the total
        total += roman_to_int_map[s[i]]

        # Step 4: If the current value is larger than the previous one, subtract twice the previous value
        if i > 0 and roman_to_int_map[s[i]] > roman_to_int_map[s[i - 1]]:
            total -= 2 * roman_to_int_map[s[i - 1]]

    return total
#time O(n)
#space O(1)
