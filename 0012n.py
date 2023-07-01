#greedy
def intToRoman(num: int) -> str:
    # List of tuples that map Roman numerals to their integer values.
    numeral_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                   (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                   (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    # Initialize the result as an empty string.
    roman = ''

    # Iterate through each numeral mapping, starting from the largest.
    for value, numeral in numeral_map:
        # While we can still subtract this numeral's value from num, do so,
        # and append this numeral to our result.
        while num >= value:
            num -= value
            roman += numeral

    # Return the result.
    return roman
#time O(1)
#space O(1)
