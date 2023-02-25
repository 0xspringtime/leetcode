def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    res = [[x, y] for y in range(cols) for x in range(rows)]
    res.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
    return res
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0,1],[1,1]],
            "expected": 1
        },
        {
            "name": "simple case 2",
            "input": [[0,1],[1,0]],
            "expected": 2
        },
        {
            "name": "list with one item",
            "input": [[0,0,0],[0,0,1],[1,1,0]],
            "expected": 2
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == allCellsDistOrder(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))