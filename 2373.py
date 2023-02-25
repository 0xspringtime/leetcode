def largestLocal(grid):
    n = len(grid)
    matrix = [[1] * (n - 2) for i in range(n - 2)]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            matrix[i - 1][j - 1] = max(grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                                       grid[i][j - 1], grid[i][j], grid[i][j + 1],
                                       grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1])
    return matrix

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]],
            "expected": [[9,9],[8,6]]
        },
        {
            "name": "simple case 2",
            "input": [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]],
            "expected": [[2,2,2],[2,2,2],[2,2,2]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == largestLocal(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))