def isCovered(ranges, left: int, right: int) -> bool:
    c = 0
    for i in range(left, right + 1):
        for j, k in ranges:
            if j <= i and i <= k:
                c += 1
                break
    return c == (right - left) + 1

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2],[3,4],[5,6]],
            "input1": 2,
            "input2": 5,
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [[1,10],[10,20]],
            "input1": 21,
            "input2": 21,
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isCovered(test_case["input"], test_case["input1"], test_case["input2"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))