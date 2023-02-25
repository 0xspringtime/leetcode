def intersection(nums):
    return sorted(set.intersection(*map(set, nums)))

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]],
            "expected": [3,4]
        },
        {
            "name": "simple case 2",
            "input": [[1,2,3],[4,5,6]],
            "expected": []
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == intersection(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))