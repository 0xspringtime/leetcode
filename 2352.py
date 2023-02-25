from typing import List
from collections import Counter
def equalPairs(grid: List[List[int]]) -> int:
    tpse = Counter(zip(*grid))  # <-- determine the transpose
    #     and hash the rows

    grid = Counter(map(tuple, grid))  # <-- hash the rows of grid. (Note the tuple-map, so
    #     we can compare apples w/ apples in next step.)

    return sum(tpse[t] * grid[t] for t in tpse)  # <-- compute the number of identical pairs

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[3,2,1],[1,7,6],[2,7,7]],
            "expected": 1
        },
        {
            "name": "simple case 2",
            "input": [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]],
            "expected": 3
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == equalPairs(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))