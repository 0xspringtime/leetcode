from typing import List
def restoreMatrix(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    col_sum = colSum
    row_sum = rowSum

    mat = [[0] * len(col_sum) for i in range(len(row_sum))]
    i = 0
    j = 0
    while i < len(row_sum) and j < len(col_sum):
        mat[i][j] = min(row_sum[i], col_sum[j])
        if row_sum[i] == col_sum[j]:
            i += 1
            j += 1
        elif row_sum[i] > col_sum[j]:
            row_sum[i] -= col_sum[j]
            j += 1
        else:
            col_sum[j] -= row_sum[i]
            i += 1

    return mat

def restoreMatrix1(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    n, m = len(rowSum), len(colSum)
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]
    return matrix

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input1": [3,8], 
            "input2": [4,7],
            "expected": [[3,0], [1,7]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == restoreMatrix1(test_case["input1"], test_case["input2"]), test_case["name"]
from datetime import datetime
start_time = datetime.now()
test()
print("Everything passed")
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))