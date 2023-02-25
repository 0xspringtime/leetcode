def productExceptSelf(nums):
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,2,3,4],
            "expected": [24,12,8,6]
        },
        {
            "name": "simple case 2",
            "input": [-1,1,0,-3,3],
            "expected": [0,0,9,0,0]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == productExceptSelf(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))