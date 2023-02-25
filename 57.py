from typing import List
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i = 0
    while (i < len(intervals) and intervals[i][0] < newInterval[0]):
        i += 1

    intervals.insert(i, newInterval)

    ans = []
    for interval in intervals:
        if len(ans) == 0 or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
    return ans
#0(n)

def insert1(intervals: List[List[int]], newInterval: List[int]
) -> List[List[int]]:
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
    res.append(newInterval)
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,3],[6,9]],
            "input1": [2,5],
            "expected": [[1,5],[6,9]]
        },
        {
            "name": "simple case 2",
            "input": [[1,2],[3,5],[6,7],[8,10],[12,16]],
            "input1": [4,8],
            "expected": [[1,2],[3,10],[12,16]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == insert1(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))