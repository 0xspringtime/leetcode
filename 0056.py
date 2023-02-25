from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += [i]
    return out
#O(nlogn)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,3],[2,6],[8,10],[15,18]],
            "expected": [[1,6],[8,10],[15,18]]
        },
        {
            "name": "simple case 2",
            "input": [[1,4],[4,5]],
            "expected": [[1,5]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == merge(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
