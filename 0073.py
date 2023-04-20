def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = set()
    column = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)
    for i in row:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for i in column:
        for j in range(len(matrix)):
            matrix[j][i] = 0
    return matrix

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,1,1],[1,0,1],[1,1,1]],
            "expected":  [[1,0,1],[0,0,0],[1,0,1]]
        },
        {
            "name": "simple case 2",
            "input": [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
            "expected": [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == setZeroes(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
