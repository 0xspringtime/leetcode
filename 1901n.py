#binary search
#divide and conquer
def findPeakGrid(mat):
    m, n = len(mat), len(mat[0])

    # function to get max element in a column
    def get_max_col(col):
        max_val = max(mat[i][col] for i in range(m))
        max_idx = [i for i in range(m) if mat[i][col] == max_val][0]
        return max_idx, max_val

    # binary search function
    def binary_search(l, r):
        mid = l + (r - l) // 2
        max_row, _ = get_max_col(mid)

        # check if the current column element is a peak
        if (mid == 0 or mat[max_row][mid] > mat[max_row][mid - 1]) and (mid == n - 1 or mat[max_row][mid] > mat[max_row][mid + 1]):
            return [max_row, mid]

        # else, go towards the greater neighbor
        if mid > 0 and mat[max_row][mid] < mat[max_row][mid - 1]:
            return binary_search(l, mid - 1)
        else:
            return binary_search(mid + 1, r)

    return binary_search(0, n - 1)
#time O(m log n) or O(n log m)
#space O(1)
