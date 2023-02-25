def construct2DArray(original, m: int, n: int):
    return [original[i:i + n] for i in range(0, len(original), n)] if m * n == len(original) else []

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "input1": 1,
            "input2": 3,
            "expected": [[1,2,3]]
        },
        {
            "name": "simple case 1",
            "input": [1, 2],
            "input1": 1,
            "input2": 1,
            "expected": []
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == construct2DArray(test_case["input"], test_case["input1"], test_case["input2"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))