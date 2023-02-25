import bisect
def findRightInterval(intervals):
    N = len(intervals)
    res = [-1] * N

    intervals = sorted([intervals[i] + [i] for i in range(N)])
    new = [i[0] for i in intervals]

    for left, right, index in intervals:
        cur = bisect.bisect_left(new, right)
        if cur != N:
            res[index] = intervals[cur][2]

    return res
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2]],
            "expected": [-1]
        },
        {
            "name": "simple case 2",
            "input": [[3,4],[2,3],[1,2]],
            "expected": [-1,0,1]
        },
        {
            "name": "list with one item",
            "input": [[1,4],[2,3],[3,4]],
            "expected": [-1,2,-1]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == findRightInterval(test_case["input"]), test_case["name"]


if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))