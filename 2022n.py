def construct2DArray(original, m, n):
    # Check if the total number of elements is compatible with the dimensions of the 2D array
    if m * n != len(original):
        return []

    # Initialize the 2D array
    array2D = []

    # Populate the 2D array
    for i in range(m):
        start = i * n  # Starting index for the slice
        end = start + n  # Ending index for the slice
        row = original[start:end]  # Slice the original array
        array2D.append(row)  # Append the row to the 2D array

    return array2D
#time O(m)
#space O(mn)
