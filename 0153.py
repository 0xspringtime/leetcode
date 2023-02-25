def findMin(nums) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [3,4,5,1,2],
            "expected": 1
        },
        {
            "name": "simple case 2",
            "input": [4,5,6,7,0,1,2],
            "expected": 0
        },
        {
            "name": "list with one item",
            "input": [11,13,15,17],
            "expected": 11
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == findMin(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))