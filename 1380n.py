def luckyNumbers(matrix):
    # Step 1: Identify the minimum number in each row
    # min(row) for each row in matrix, convert result to a set
    min_in_rows = set(min(row) for row in matrix)

    # Step 2: Identify the maximum number in each column
    # max(column) for each column in matrix, convert result to a set
    max_in_columns = set(max(col) for col in zip(*matrix))  # zip(*matrix) transposes the matrix

    # Step 3: Find the intersection of the two sets. These are the lucky numbers.
    lucky_numbers = min_in_rows & max_in_columns  # & is the set intersection operator in Python

    # Convert the set to a list and return it
    return list(lucky_numbers)
#time O(m+n)
#space O(m+n)
