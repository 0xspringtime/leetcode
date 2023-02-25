from collections import defaultdict, deque
from itertools import accumulate
def getDistances(arr):
    n = len(arr)
    d = defaultdict(list)
    for i, v in enumerate(arr): d[v].append(i)

    res = defaultdict(list)
    for v, idx in d.items():
        ps = list(accumulate(idx, initial=0))
        vals = []
        idn = len(idx)
        for i, x in enumerate(idx):
            vals.append(i * x - ps[i] + ps[-1] - ps[i + 1] - (idn - i - 1) * x)

        res[v] = deque(vals)

    return [res[v].popleft() for v in arr]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [2,1,3,1,2,3,3],
            "expected": [4,2,7,2,4,4,5]
        },
        {
            "name": "simple case 2",
            "input": [10,5,10,10],
            "expected": [5,0,3,4]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == getDistances(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))