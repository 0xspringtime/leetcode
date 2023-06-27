def flipAndInvertImage(image):
    # The output array
    result = []
    
    # Iterate through each row in the input image
    for row in image:
        # Reverse the row
        reversed_row = row[::-1]
        
        # Invert the row by replacing 0s with 1s and 1s with 0s
        inverted_row = [1 - i for i in reversed_row]
        
        # Append the inverted row to the result
        result.append(inverted_row)
    
    return result
#time O(n^2)
#space O(n^2)
