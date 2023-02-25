def search(nums, target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [-1,0,3,5,9,12],
            "input1": 9,
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [-1,0,3,5,9,12],
            "input1": 2,
            "expected": -1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == search(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))