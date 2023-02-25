def maxIncreaseKeepingSkyline(grid) -> int:
    rows, cols = list(map(max, grid)), list(map(max, zip(*grid)))
    return sum(min(i, j) for i in rows for j in cols) - sum(map(sum, grid))


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]],
            "expected": 35
        },
        {
            "name": "simple case 2",
            "input": [[0,0,0],[0,0,0],[0,0,0]],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxIncreaseKeepingSkyline(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))