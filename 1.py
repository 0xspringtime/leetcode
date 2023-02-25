def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [2,7,11,15],
            "input1": 9,
            "expected": [0,1]
        },
        {
            "name": "simple case 2",
            "input": [3, 2, 4],
            "input1": 6,
            "expected": [1,2]
        },
        {
            "name": "simple case 3",
            "input": [3,3],
            "input1": 6,
            "expected": [0,1]
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == twoSum(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))