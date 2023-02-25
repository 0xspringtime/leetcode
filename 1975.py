def maxMatrixSum(matrix) -> int:
    arr = [num for row in matrix for num in row]
    abs_total = sum(map(abs, arr))
    neg = sum([num < 0 for num in arr])
    mi = min(map(abs, arr))
    return abs_total if neg % 2 == 0 else abs_total - 2 * mi

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,-1],[-1,1]],
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [[1,2,3],[-1,-2,-3],[1,2,3]],
            "expected": 16
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxMatrixSum(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))