def islandPerimeter(grid) -> int:
    M, N, p = len(grid), len(grid[0]), 0
    for m in range(M):
        for n in range(N):
            if grid[m][n] == 1:
                if m == 0 or grid[m - 1][n] == 0: p += 1
                if n == 0 or grid[m][n - 1] == 0: p += 1
                if n == N - 1 or grid[m][n + 1] == 0: p += 1
                if m == M - 1 or grid[m + 1][n] == 0: p += 1
    return p

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],
            "expected":16
        },
        {
            "name": "simple case 2",
            "input": [[1]],
            "expected": 4
        },
        {
            "name": "list with one item",
            "input": [[1,0]],
            "expected":4
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == islandPerimeter(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))