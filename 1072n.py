#hash
def maxEqualRowsAfterFlips(matrix):
    # dictionary to store the frequency of each row
    row_dict = {}

    for row in matrix:
        # convert the row to a tuple
        row_tuple = tuple(row)
        # find the inverse of the row
        inv_tuple = tuple(1 - i for i in row)

        # if the row is in the dictionary, increment its count
        if row_tuple in row_dict:
            row_dict[row_tuple] += 1
        else:
            row_dict[row_tuple] = 1

        # if the inverse row is in the dictionary, increment its count
        if inv_tuple in row_dict:
            row_dict[inv_tuple] += 1
        else:
            row_dict[inv_tuple] = 1

    # return the maximum frequency
    return max(row_dict.values())
#time O(m*n)
#space O(m)
