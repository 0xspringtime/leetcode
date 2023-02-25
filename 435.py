def eraseOverlapIntervals(intervals) -> int:
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res
#O(nlogn)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2],[2,3],[3,4],[1,3]],
            "expected": 1
        },
        {
            "name": "simple case 2",
            "input": [[1,2],[1,2],[1,2]],
            "expected": 2
        },
        {
            "name": "list with one item",
            "input": [[1,2],[2,3]],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == eraseOverlapIntervals(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))