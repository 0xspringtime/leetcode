from typing import List
def matrixBlockSum(mat, k):
    col = len(mat[0])
    row = len(mat)
    new_mat = [[0] * col for i in range(0, row)]

    for i in range(row):
        for j in range(col):
            new_mat[i][j] = sum(
                [sum(ele[max(j - k, 0):min(j + k + 1, col)]) for ele in mat[max(i - k, 0):min(i + k + 1, row)]])

    return new_mat
#O(mn)

def matrixBlockSum1(mat: List[List[int]], K: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    mat[:] = [[0] * (n + 1)] + [[0] + row for row in mat]
    res = [[0] * n for i in range(m)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]

    for i in range(m):
        for j in range(n):
            r1, r2 = max(i - K, 0), min(i + K + 1, m)
            c1, c2 = max(j - K, 0), min(j + K + 1, n)
            res[i][j] = mat[r2][c2] - mat[r2][c1] - mat[r1][c2] + mat[r1][c1]

    return res
#O(mn)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "input1": 1,
            "expected": [[12,21,16],[27,45,33],[24,39,28]]
        },
        {
            "name": "simple case 2",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "input1": 2,
            "expected": [[45,45,45],[45,45,45],[45,45,45]] 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == matrixBlockSum1(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))