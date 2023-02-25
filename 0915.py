def partitionDisjoint(nums):
    l, r = 0, 0
    LENGTH = len(nums)
    largest = nums[0]
    while r < LENGTH - 1:
        while r + 1 < LENGTH and nums[r + 1] >= largest:
            r += 1
        l = l + 1
        r = l if l > r else r
        largest = max(nums[l], largest)
    return l
#O(N)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [5,0,3,8,6],
            "expected": 3
        },
        {
            "name": "simple case 2",
            "input": [1,1,1,0,6,12],
            "expected": 4
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == partitionDisjoint(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))