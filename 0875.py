from math import *
def minEatingSpeed(piles, h: int) -> int:
    l, r = 1, max(piles)
    res = max(piles)

    while l <= r:
        k = (l + r) // 2

        totalTime = 0
        for p in piles:
            totalTime += ceil(p / k)
        if totalTime <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [3,6,7,11],
            "input1": 8,
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [30,11,23,4,20],
            "input1": 5,
            "expected": 30
        },
        {
            "name": "simple case 3",
            "input": [30,11,23,4,20],
            "input1": 6,
            "expected": 23
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == minEatingSpeed(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    test()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))