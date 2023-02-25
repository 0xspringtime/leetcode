def checkXMatrix(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                if grid[i][j] == 0: return False
            else:
                if grid[i][j] != 0: return False
    return True


# O(n^2)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]],
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [[5, 7, 0], [0, 3, 1], [0, 5, 0]],
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == checkXMatrix(test_case["input"]), test_case["name"]


from datetime import datetime

start_time = datetime.now()
test()
print("Everything passed")
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
