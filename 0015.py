def threeSum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [-1,0,1,2,-1,-4],
            "expected": [[-1,-1,2],[-1,0,1]]
        },
        {
            "name": "simple case 2",
            "input": [0,1,1],
            "expected": []
        },
        {
            "name": "list with one item",
            "input": [0,0,0],
            "expected": [[0,0,0]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == threeSum(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))