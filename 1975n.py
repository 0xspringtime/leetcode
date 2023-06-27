#greedy
def maxMatrixSum(matrix):
    # We'll keep track of the smallest absolute value in the matrix and count of negative numbers.
    min_abs_val = float('inf')
    negative_count = 0
    sum = 0

    # Iterate over each cell in the matrix.
    for row in matrix:
        for val in row:
            # Update the smallest absolute value if necessary.
            min_abs_val = min(min_abs_val, abs(val))

            # Count the number of negative numbers.
            if val < 0:
                negative_count += 1

            # Add the absolute value of the current element to the sum.
            sum += abs(val)

    # If the count of negative numbers is odd, subtract twice the smallest absolute value from the sum.
    # This is equivalent to flipping the smallest absolute value in the matrix.
    if negative_count % 2 == 1:
        sum -= 2 * min_abs_val

    return sum
#time O(n^2)
#space O(1)
