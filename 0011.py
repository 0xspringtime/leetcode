def maxArea(height) -> int:
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        elif height[r] <= height[l]:
            r -= 1
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,8,6,2,5,4,8,3,7],
            "expected": 49
        },
        {
            "name": "simple case 2",
            "input": [1, 1],
            "expected": 1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxArea(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))