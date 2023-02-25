def removeCoveredIntervals(intervals) -> int:
    res = right = 0
    intervals.sort(key=lambda a: (a[0], -a[1]))
    for i, j in intervals:
        res += j > right
        right = max(right, j)
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,4],[3,6],[2,8]],
            "expected": 2
        },
        {
            "name": "simple case 2",
            "input": [[1,4],[2,3]],
            "expected": 1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == removeCoveredIntervals(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))