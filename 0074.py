from bisect import bisect_left
def searchMatrix(matrix, target: int) -> bool:
    r = bisect_left(matrix, target, key=lambda row: row[-1])  # or key=itemgetter(-1)
    return r < len(matrix) and matrix[r][bisect_left(matrix[r], target)] == target

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            "input1": 3,
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            "input1": 13,
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == searchMatrix(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    test()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
