def average(L):


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "input1": 2,
            "expected": 2.0
        },
        {
            "name": "simple case 2",
            "input": [1, 2, 3, 4],
            "input1": 3,
            "expected": 2.5
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == average(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
