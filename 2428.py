def maxSum(grid) -> int:
    res = 0
    cur = 0

    for i in range(len(grid) - 2):
        for j in range(1, len(grid[0]) - 1):
            cur = sum(grid[i][j - 1:j + 2]) + grid[i + 1][j] + sum(grid[i + 2][j - 1:j + 2])
            res = max(res, cur)

    return res
#O(n*m)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]],
            "expected": 30
        },
        {
            "name": "simple case 2",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "expected": 35
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxSum(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))