def minGroups(intervals):
    A = []
    for a,b in intervals:
        A.append([a,1])
        A.append([b+1,-1])
    res = cur = 0
    for a, diff in sorted(A):
        cur += diff
        res = max(res, cur)
    return res
#O(nlogn)
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[5,10],[6,8],[1,5],[2,3],[1,10]],
            "expected": 3
        },
        {
            "name": "simple case 2",
            "input": [[1,3],[5,6],[8,10],[11,13]],
            "expected": 1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == minGroups(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))