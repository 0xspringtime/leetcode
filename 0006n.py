#string
def convert(s, numRows):
    # If there's only one row, the zigzag pattern is the same as the original string.
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize an array of empty strings, one for each row.
    rows = [""] * numRows
    index, step = 0, 1

    # Iterate over the characters in the string.
    for char in s:
        # Append the current character to the current row's string.
        rows[index] += char
        
        # If we've reached the bottom row, change direction to go up.
        # If we've reached the top row, change direction to go down.
        if index == 0:
            step = 1
        elif index == numRows -1:
            step = -1
            
        # Move to the next row.
        index += step

    # Concatenate the row strings and return the result.
    return "".join(rows)
#time O(n)
#space O(n)
