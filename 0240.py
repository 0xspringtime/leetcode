def searchMatrix(matrix, target: int) -> bool:
    j = -1
    for row in matrix:
        while j + len(row) and row[j] > target:
            j -= 1
        if row[j] == target:
            return True
    return False

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
            "input1": 5,
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
            "input1": 20,
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == searchMatrix(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))