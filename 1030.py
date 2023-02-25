from typing import List
def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    res = [[x, y] for y in range(cols) for x in range(rows)]
    res.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
    return res

def test():
    test_cases = [
    {
        "name": "example 1",
        "input": 1,
        "input1": 2,
        "input2": 0,
        "input3": 0,
        "expected": [[0,0],[0,1]]
    },
    {
        "name": "example 2",
        "input": 2,
        "input1": 2,
        "input2": 0,
        "input3": 1,
        "expected": [[0,1],[0,0],[1,1],[1,0]]
    }
]
    for test_case in test_cases:
        assert test_case["expected"] == allCellsDistOrder(test_case["input"], test_case["input1"], test_case["input2"], test_case["input3"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
