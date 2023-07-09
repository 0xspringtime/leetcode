#greedy
def reconstructMatrix(upper, lower, colsum):
    n = len(colsum)
    upper_row, lower_row = [0]*n, [0]*n

    # first pass, set columns with sum 2
    for i in range(n):
        if colsum[i] == 2:
            upper_row[i] = lower_row[i] = 1
            upper -= 1
            lower -= 1

    # second pass, set columns with sum 1
    for i in range(n):
        if colsum[i] == 1:
            if upper > 0:  # set upper row first
                upper_row[i] = 1
                upper -= 1
            else:  # then set lower row
                lower_row[i] = 1
                lower -= 1

    # if we have used up exactly upper and lower, return the matrix
    if upper == 0 and lower == 0:
        return [upper_row, lower_row]
    else:
        return []
#time O(n)
#space O(n)
