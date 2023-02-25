def search(nums, target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [4,5,6,7,0,1,2],
            "input1": 0,
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [4,5,6,7,0,1,2],
            "input1": 3,
            "expected": -1
        },
        {
            "name": "simple case 3",
            "input": [1],
            "input1": 0,
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
