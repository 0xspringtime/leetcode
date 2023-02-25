def twoSum(numbers, target: int):
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [2,7,11,15],
            "input1": 9,
            "expected": [1,2]
        },
        {
            "name": "simple case 2",
            "input": [2,3,4],
            "input1": 6,
            "expected": [1,3]
        },
        {
            "name": "list with one item",
            "input": [-1,0],
            "input1": -1,
            "expected": [1,2]
        }
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